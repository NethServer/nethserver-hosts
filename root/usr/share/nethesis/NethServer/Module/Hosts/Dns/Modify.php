<?php

namespace NethServer\Module\Hosts\Dns;

/*
 * Copyright (C) 2014  Nethesis S.r.l.
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
 * Modify host records
 *
 * @author Davide Principi <davide.principi@nethesis.it>
 * @since 1.0
 */
class Modify extends \Nethgui\Controller\Table\Modify
{

    public function initialize()
    {
        $parameterSchema = array(
            array('hostname', Validate::HOSTNAME_FQDN, \Nethgui\Controller\Table\Modify::KEY),
            array('IpAddress', Validate::IPv4, \Nethgui\Controller\Table\Modify::FIELD),
            array('Description', Validate::ANYTHING, \Nethgui\Controller\Table\Modify::FIELD),
        );
        $this->setSchema($parameterSchema);
        parent::initialize();
    }

    public function validate(\Nethgui\Controller\ValidationReportInterface $report)
    {
        if ($this->getIdentifier() === 'delete') {
            $v = $this->createValidator()->platform('host-delete', 'hosts');
            if ( ! $v->evaluate($this->parameters['hostname'])) {
                $report->addValidationError($this, 'Key', $v);
            }
        }
        parent::validate($report);
    }

    protected function onParametersSaved($parameters)
    {
        $actionName = $this->getIdentifier();
        if ($actionName === 'update') {
            $actionName = 'modify';
        }
        $this->getPlatform()->signalEvent(sprintf('host-%s &', $actionName));
    }

    public function prepareView(\Nethgui\View\ViewInterface $view)
    {
        parent::prepareView($view);
        $templates = array(
            'create' => 'NethServer\Template\Hosts\Dns',
            'update' => 'NethServer\Template\Hosts\Dns',
            'delete' => 'Nethgui\Template\Table\Delete',
        );
        $view->setTemplate($templates[$this->getIdentifier()]);
    }

}
