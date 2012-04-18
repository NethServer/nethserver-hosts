<?php

echo $view->panel()
        ->insert($view->header('address')->setAttribute('template', 'Host entry'))
        ->insert($view->textInput('hostname'))
        ->insert($view->textInput('Description'))
        ->insert($view->hidden('HostType'));

        
echo $view->buttonList($view::BUTTON_SUBMIT | $view::BUTTON_CANCEL);
