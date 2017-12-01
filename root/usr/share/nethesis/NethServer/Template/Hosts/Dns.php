<?php
/* @var $view \Nethgui\Renderer\Xhtml */

if ($view->getModule()->getIdentifier() == 'update') {
    $keyFlags = $view::STATE_DISABLED;
    $template = 'Update_Dns_Header';
} else {
    $keyFlags = 0;
    $template = 'Create_Dns_Header';
}

echo $view->header('hostname')->setAttribute('template', $T($template));

echo $view->panel()
        ->insert($view->columns()
        ->insert($view->textInput('hostname', $keyFlags))
        ->insert($view->checkbox('WildcardMode', 'enabled')->setAttribute('uncheckedValue', 'disabled'))
        )
        ->insert($view->textInput('IpAddress'))
        ->insert($view->textInput('Description'))
;
        
echo $view->buttonList($view::BUTTON_SUBMIT | $view::BUTTON_CANCEL | $view::BUTTON_HELP);
