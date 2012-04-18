<?php
namespace NethServer\Module\Hosts;

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

/**
 * Implement gui module for /etc/hosts configuration
 */
class Dns extends \Nethgui\Controller\TableController
{

    public function initialize()
    {
        $columns = array(
            'Key',
            'IPAddress',
            'Comment',
            'Actions',
        );

        $parameterSchema = array(
            array('hostname', Validate::HOSTNAME_FQDN, \Nethgui\Controller\Table\Modify::KEY),
            array('IPAddress', Validate::IPv4, \Nethgui\Controller\Table\Modify::FIELD),
            array('Description', Validate::ANYTHING, \Nethgui\Controller\Table\Modify::FIELD, 'Comment'),
            array('HostType', '/^Remote$/', \Nethgui\Controller\Table\Modify::FIELD),            
        );

        $this
            ->setTableAdapter($this->getPlatform()->getTableAdapter('hosts', 'host', array('HostType' => "/^Remote$/")))
            ->setColumns($columns)
            ->addRowAction(new \Nethgui\Controller\Table\Modify('update', $parameterSchema, 'NethServer\Template\Hosts\Dns'))
            ->addRowAction(new \Nethgui\Controller\Table\Modify('delete', $parameterSchema, 'Nethgui\Template\Table\Delete')) // Standard DELETE template
            ->addTableAction(new \Nethgui\Controller\Table\Modify('create', $parameterSchema, 'NethServer\Template\Hosts\Dns'))
            ->addTableAction(new \Nethgui\Controller\Table\Help('Help'))
        ;

        $this->getAction('create')->setCreateDefaults(array('HostType' => 'Remote'));

        parent::initialize();
    }

    public function onParametersSaved(\Nethgui\Module\ModuleInterface $currentAction, $changes, $parameters)
    {
        $actionName = $currentAction->getIdentifier();
        if($actionName === 'update') {
            $actionName = 'modify';
        }
        $this->getPlatform()->signalEvent(sprintf('host-%s@post-process', $actionName));
    }

}
