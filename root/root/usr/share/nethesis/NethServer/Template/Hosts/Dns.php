<?php

echo $view->panel()
        ->insert($view->header('address')->setAttribute('template', 'Host entry'))
        ->insert($view->textInput('hostname', ($view->getModule()->getIdentifier() == 'update' ? $view::STATE_READONLY : 0)))
        ->insert($view->textInput('IPAddress'))
        ->insert($view->hidden('HostType'));

        
echo $view->buttonList($view::BUTTON_SUBMIT | $view::BUTTON_CANCEL);
