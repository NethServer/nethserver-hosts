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
 * Implement gui module for localhost alias in /etc/hosts.
 */
class Alias extends \Nethgui\Controller\TableController
{

    public function initialize()
    {
        $columns = array(
            'Key',
            'Actions',
        );

        $parameterSchema = array(
            array('hostname', Validate::HOSTNAME_FQDN, \Nethgui\Controller\Table\Modify::KEY),
            array('HostType', '/^Self$/', \Nethgui\Controller\Table\Modify::FIELD),
        );

        $this
            ->setTableAdapter($this->getPlatform()->getTableAdapter('hosts', 'host', array('HostType' => '/^Self$/')))
            ->setColumns($columns)
            ->addRowAction(new \Nethgui\Controller\Table\Modify('delete', $parameterSchema, 'Nethgui\Template\Table\Delete'))
            ->addTableAction(new \Nethgui\Controller\Table\Modify('create', $parameterSchema, 'NethServer\Template\Hosts\Alias'))
            ->addTableAction(new \Nethgui\Controller\Table\Help('Help'))
        ;

        $this->getAction('create')->setCreateDefaults(array('HostType' => 'Self'));

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
