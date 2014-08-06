<?php
namespace NethServer\Module\Hosts\Dns;

/*
 * Copyright (C) 2012 Nethesis S.r.l.
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
 * TODO: add component description here
 *
 * @author Davide Principi <davide.principi@nethesis.it>
 * @since 1.0
 */
class Configure extends \Nethgui\Controller\Table\AbstractAction
{

    private $nameservers;   
 
    public function initialize()
    {
        $this->nameservers = $this->getPlatform()->getIdentityAdapter('configuration', 'dns', 'NameServers', ',');
        $this->declareParameter('Dns1', Validate::IPv4, array());
        $this->declareParameter('Dns2', $this->createValidator()->orValidator(
                                            $this->createValidator(Validate::IPv4),$this->createValidator()->maxLength(0)
                                        ), 
                                        array()
        );
    }

    protected function onParametersSaved($changedParameters)
    {
        $this->nameservers->save();
        $this->getPlatform()->signalEvent('nethserver-hosts-save');
    }

    public function readDns1()
    {
       return isset($this->nameservers[0])?$this->nameservers[0]:''; 
    }

    public function readDns2()
    {
       return isset($this->nameservers[1])?$this->nameservers[1]:''; 
    }

    public function writeDns1($v)
    {
       $this->nameservers[0] = $v; 
       return TRUE; 
    }

    public function writeDns2($v)
    {
       if(!$v) {
           unset($this->nameservers[1]);
       } else {
           $this->nameservers[1] = $v;
       }
       return TRUE;
    }

}
