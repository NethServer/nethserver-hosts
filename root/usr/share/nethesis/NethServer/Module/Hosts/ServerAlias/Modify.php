<?php

namespace NethServer\Module\Hosts\ServerAlias;

/*
 * Copyright (C) 2016  Nethesis S.r.l.
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
 * @contributor stephane de Labrusse <stephdl@de-labrusse.fr>
 */
class Modify extends \Nethgui\Controller\Table\Modify
{

    public function initialize()
    {
        $parameterSchema = array(
            array('hostname', Validate::HOSTNAME_FQDN, \Nethgui\Controller\Table\Modify::KEY),
            array('Description', Validate::ANYTHING, \Nethgui\Controller\Table\Modify::FIELD),
        );
        $this->setSchema($parameterSchema);
        parent::initialize();
    }

    public function validate(\Nethgui\Controller\ValidationReportInterface $report)
    {
        if ($this->getIdentifier() === 'delete') {
            $v = $this->createValidator()->platform('host-delete');
            if ( ! $v->evaluate($this->parameters['hostname'])) {
                $report->addValidationError($this, 'Key', $v);
            }
        }

        #a key can be  'remote or self' and must not be overwritten
        $keyExists = $this->getPlatform()->getDatabase('hosts')->getType($this->parameters['hostname']) != '';
        if($this->getIdentifier() === 'create' && $keyExists) {
        $report->addValidationErrorMessage($this, 'hostname', 'Service_key_exists_message');
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
            'create' => 'NethServer\Template\Hosts\ServerAlias',
            'update' => 'NethServer\Template\Hosts\ServerAlias',
            'delete' => 'Nethgui\Template\Table\Delete',
        );
        $view->setTemplate($templates[$this->getIdentifier()]);
    }

}
