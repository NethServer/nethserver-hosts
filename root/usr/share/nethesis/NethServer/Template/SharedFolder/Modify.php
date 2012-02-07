<?php
if ($view->getModule()->getIdentifier() == 'update') {
    $keyFlags = $view::STATE_READONLY;
    $template = 'Edit shared folder `${0}`';
} else {
    $keyFlags = 0;
    $template = 'Create a new shared folder';
}

echo $view->header('ibay')->setAttribute('template', $view->translate($template));
$baseTab = $view->panel()->setAttribute('name', "BaseInfo")
    ->insert($view->textInput('ibay', $keyFlags))
    ->insert($view->textInput('Name'))
    ->insert($view->selector('Group', $view::SELECTOR_DROPDOWN)->setAttribute('choices', 'OwnersDatasource'));

$baseTabColumnSet1 = $view->columns();
$baseTab->insert($baseTabColumnSet1);

$baseTabColumnSet1->insert($view->fieldset()->setAttribute('template', 'Recycle')
        ->insert($view->fieldsetSwitch('RecycleBin', 'enabled')
            ->insert($view->checkBox('KeepVersions', 'enabled')->setAttribute('uncheckedValue', 'disabled'))
        )
        ->insert($view->fieldsetSwitch('RecycleBin', 'disabled')));

$baseTabColumnSet1->insert($view->fieldset()->setAttribute('template', 'Shadow copy')
        ->insert($view->fieldsetSwitch('ShadowCopy', 'enabled'))
        ->insert($view->fieldsetSwitch('ShadowCopy', 'disabled')));

$baseTab->insert($view->fieldset()->setAttribute('template', 'Web server options') // ->setAttribute('icon-before', 'ui-icon-link')
        ->insert($view->checkBox('CgiBin', 'enabled')->setAttribute('uncheckedValue', 'disabled')));

$permissionTab = $view->panel()->setAttribute('name', 'Permissions')
    ->insert($view->columns()
    ->insert($view->fieldset()->setAttribute('template', 'Read permissions') //->setAttribute('icon-before', 'ui-icon-folder-open')
        ->insert($view->radioButton('read', 'admin'))
        ->insert($view->radioButton('read', 'group'))
        ->insert($view->radioButton('read', 'everyone')))
    ->insert($view->fieldset()->setAttribute('template', 'Write permissions') //->setAttribute('icon-before', 'ui-icon-locked')->setAttribute('icon-before', 'ui-icon-disk')
        ->insert($view->radioButton('write', 'admin'))
        ->insert($view->radioButton('write', 'group'))
        ->insert($view->radioButton('write', 'everyone')))
);


$permissionTab->insert($view->fieldset()->setAttribute('template', 'Access control') // ->setAttribute('icon-before', 'ui-icon-locked')
        ->insert($view->fieldsetSwitch('access', 'local')
            ->insert($view->checkBox('local_password', 'pw')))
        ->insert($view->fieldsetSwitch('access', 'global')
            ->insert($view->radioButton('global_password', 'pw'))
            ->insert($view->radioButton('global_password', 'pw-remote'))
            ->insert($view->radioButton('global_password', '')))
);

$aclTab = $view->panel()->setAttribute('name', "Acl")
    ->insert($view->objectPicker()
    ->setAttribute('objects', 'AclSubjects')
    ->insert($view->checkBox('AclRead', FALSE, $view::STATE_CHECKED))
    ->insert($view->checkBox('AclWrite', FALSE))
);

echo $view->tabs()->insert($baseTab)->insert($permissionTab)->insert($aclTab);

echo $view->buttonList($view::BUTTON_SUBMIT | $view::BUTTON_CANCEL | $view::BUTTON_HELP);

