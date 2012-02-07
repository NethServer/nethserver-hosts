<?php
namespace NethServer\Module;

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
 * iBays management module
 * 
 * @author Giacomo Sanchietti <giacomo@nethesis.it>
 */
class SharedFolder extends \Nethgui\Controller\TableController
{

    protected function initializeAttributes(\Nethgui\Module\ModuleAttributesInterface $base)
    {
        return \Nethgui\Module\SimpleModuleAttributesProvider::extendModuleAttributes($base, 'Management', 30);
    }

    public function initialize()
    {
        $columns = array(
            'Key',
            'Name',
            'Actions'
        );

        $this
            ->setTableAdapter($this->getPlatform()->getTableAdapter('accounts', 'ibay'))
            ->setColumns($columns)
            ->addTableAction(new SharedFolder\Modify('create'))
            ->addTableAction(new \Nethgui\Controller\Table\Help('Help'))
            ->addRowAction(new SharedFolder\Modify('update'))
            ->addRowAction(new SharedFolder\Modify('delete'))
        ;
        parent::initialize();
    }

}

