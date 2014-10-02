<?php
/* @var $view \Nethgui\Renderer\Xhtml */

if ($view->getModule()->getIdentifier() == 'update') {
    $keyFlags = $view::STATE_DISABLED;
    $template = 'Update_Alias_Header';
} else {
    $keyFlags = 0;
    $template = 'Create_Alias_Header';
}

echo $view->header('hostname')->setAttribute('template', $T($template));

echo $view->panel()
        ->insert($view->textInput('hostname', $keyFlags))
        ->insert($view->textInput('Description'))
;
        
echo $view->buttonList($view::BUTTON_SUBMIT | $view::BUTTON_CANCEL | $view::BUTTON_HELP);
