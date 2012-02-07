<?php
namespace NethServer\Module\SharedFolder;

/*
 * Copyright (C) 2011 Nethesis S.r.l.
 * 
 * This script is part of NethServer.
 * 
 * NethServer is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * NethServer is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with NethServer.  If not, see <http://www.gnu.org/licenses/>.
 */

use Nethgui\System\PlatformInterface as Validate;
use Nethgui\Controller\Table\Modify as Table;

/**
 * This class manage shared folder
 *
 * @since 1.0
 */
class Modify extends \Nethgui\Controller\Table\Modify
{

    public function initialize()
    {
        $parameterSchema = array(
            array('ibay', Validate::USERNAME, Table::KEY),
            array('Name', Validate::ANYTHING, Table::FIELD),
            array('Group', Validate::USERNAME, Table::FIELD),
            array('CgiBin', Validate::SERVICESTATUS, Table::FIELD),
            array('UserAccess', false, Table::FIELD), //possibile values: global|global-pw|global-pw-remote|local|local-pw|none
            array('PublicAccess', false, Table::FIELD), //possibile values: wr-admin-rd-group|wr-group-rd-everyone|wr-group-rd-group
            array('access', '/global|local/', null), // do not map on any datasource
            array('local_password', '/^(pw|)$/', null),
            array('global_password', '/^(pw|pw-remote|)$/', null),
            array('read', '/^(admin|group|everyone)$/', null),
            array('write', '/^(admin|group|everyone)$/', null),
            array('OwnersDatasource', false, null),
            array('ShadowCopy', Validate::SERVICESTATUS, Table::FIELD),
            array('RecycleBin', Validate::SERVICESTATUS, Table::FIELD),
            array('KeepVersions', Validate::SERVICESTATUS, Table::FIELD),
            array('AclRead', Validate::USERNAME_COLLECTION, Table::FIELD, 'AclRead', ','), // ACL
            array('AclWrite', Validate::USERNAME_COLLECTION, Table::FIELD, 'AclWrite', ','), // ACL
            array('AclSubjects', FALSE, null),
        );

        $this->setSchema($parameterSchema);
        parent::initialize();
    }

    private function composeUserAccess()
    {
        return sprintf("wr-%s-rd-%s", $this->parameters['write'], $this->parameters['read']);
    }

    private function assignUserAccess($value)
    {
        if (is_null($value)) {
            // default values
            $this->parameters['read'] = 'everyone';
            $this->parameters['write'] = 'everyone';
        } else {
            $parts = explode('-', $value);
            $this->parameters['read'] = $parts[3];
            $this->parameters['write'] = $parts[1];
        }
    }

    private function composePublicAccess()
    {
        $value = $this->parameters['access'];

        if ($value == 'local' && $this->parameters['local_password']) {
            $value .= '-' . $this->parameters['local_password'];
        } elseif ($value == 'global' && $this->parameters['global_password']) {
            $value .= '-' . $this->parameters['global_password'];
        }

        return $value;
    }

    private function assignPublicAccess($value)
    {
        if (is_null($value)) {
            // default values
            $this->parameters['access'] = 'local';
            $this->parameters['local_password'] = '';
            $this->parameters['global_password'] = '';
            $value = $this->composePublicAccess();
        } else {
            $parts = explode('-', $value, 2);
            if ($parts[0] == 'local') {
                $this->parameters['access'] = 'local';
                $this->parameters['local_password'] = isset($parts[1]) ? $parts[1] : '';
                $this->parameters['global_password'] = NULL;
            } elseif ($parts[0] == 'global') {
                $this->parameters['access'] = 'global';
                $this->parameters['local_password'] = NULL;
                $this->parameters['global_password'] = isset($parts[1]) ? $parts[1] : '';
            }
        }
    }

    // TODO: validate: check iBay name uniqueness
    public function bind(\Nethgui\Controller\RequestInterface $request)
    {
        parent::bind($request);
        if ($request->isMutation()) {
            if ($this->getIdentifier() != "delete") { //do not set props if we are deleting the ibay
                $this->parameters['UserAccess'] = $this->composeUserAccess();
                $this->parameters['PublicAccess'] = $this->composePublicAccess();
            }
        } else {
            $this->assignPublicAccess($this->parameters['PublicAccess']);
            $this->assignUserAccess($this->parameters['UserAccess']);

            if (is_null($this->parameters['Group'])) {
                $this->parameters['Group'] = 'shared';
            }
            if (is_null($this->parameters['ShadowCopy'])) {
                $this->parameters['ShadowCopy'] = 'disabled';
            }
            if (is_null($this->parameters['RecycleBin'])) {
                $this->parameters['RecycleBin'] = 'disabled';
            }
            if (is_null($this->parameters['KeepVersions'])) {
                $this->parameters['KeepVersions'] = 'disabled';
            }
        }
    }

    protected function onParametersSaved($changedParameters)
    {
        $this->getPlatform()->signalEvent(sprintf('ibay-%s@post-process', $this->getIdentifier()), array(array($this, 'provideIbayName')));
    }

    /**
     * This callback function provides the argument for smedb events
     * @return string
     */
    public function provideIbayName()
    {
        return $this->getRequest()->getParameter('ibay');
    }

    public function prepareView(\Nethgui\View\ViewInterface $view)
    {
        parent::prepareView($view);
        $templates = array(
            'create' => 'NethServer\Template\SharedFolder\Modify',
            'update' => 'NethServer\Template\SharedFolder\Modify',
            'delete' => 'Nethgui\Template\Table\Delete',
        );
        $view->setTemplate($templates[$this->getIdentifier()]);

        $owners = array(array('shared', 'Everyone'), array('admin', 'Administrator'));
        $subjects = array(array('shared', 'Everyone'));

        foreach ($this->getPlatform()->getDatabase('accounts')->getAll('group') as $keyName => $props) {
            $entry = array($keyName, sprintf("%s (%s)", $props['Description'], $keyName));
            $owners[] = $entry;
            $subjects[] = $entry;
        }

        $view['OwnersDatasource'] = $owners;

        foreach ($this->getPlatform()->getDatabase('accounts')->getAll('user') as $keyName => $props) {
            $entry = array($keyName, sprintf("%s (%s)", trim($props['FirstName'] + ' ' + $props['LastName']), $keyName));
            $subjects[] = $entry;
        }

        $view['AclSubjects'] = $subjects;
    }

}

