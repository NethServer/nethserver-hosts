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

/**
 * Implement gui module for /etc/hosts configuration
 */
class Dns extends \Nethgui\Controller\TableController
{

    public function initialize()
    {
        $columns = array(
            'Key',
            'IpAddress',
            'WildcardMode',
            'Description',
            'Actions',
        );

        $this
            ->setTableAdapter($this->getPlatform()->getTableAdapter('hosts', 'remote'))
            ->setColumns($columns)
            ->addRowAction(new \NethServer\Module\Hosts\Dns\Modify('update'))
            ->addRowAction(new \NethServer\Module\Hosts\Dns\Modify('delete'))
            ->addTableAction(new \NethServer\Module\Hosts\Dns\Modify('create'))
            ->addTableAction(new \Nethgui\Controller\Table\Help('Help'))
        ;

        parent::initialize();
    }

    public function prepareViewForColumnWildcardMode(\Nethgui\Controller\Table\Read $action, \Nethgui\View\ViewInterface $view, $key, $values, &$rowMetadata)
    {
        if ($values['WildcardMode'] == 'enabled' ) {
            return $view->translate('Enabled_label');
        }
        return $view->translate('Disabled_label');
    }
}
