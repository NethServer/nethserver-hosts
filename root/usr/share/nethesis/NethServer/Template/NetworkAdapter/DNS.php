<?php

echo $view->header()->setAttribute('template', $T('Dns_Configure_header'));

echo $view->textInput('Dns1', 'disabled')->setAttribute('label', $T('dns1_label'));
echo $view->textInput('Dns2', 'disabled')->setAttribute('label', $T('dns2_label'));

echo $view->buttonList($view::BUTTON_SUBMIT | $view::BUTTON_CANCEL | $view::BUTTON_HELP);
