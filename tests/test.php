<?php
include 'php/Sport.php' ;
include 'php/Config.php' ;
include 'php/HomeItemList.php' ;

$sport = new Sport ;

$sport->setCouleur("#ffaff");



$auth = new ConfigAutorisations ;
$network = new ConfigNetwork ;
$startUp = new ConfigStart ;

$startUp->setWebviewUrl('http://test.com');
$startUp->setShowWebView(true);


$config = new Config ;

$config->setPeriodesAutorisations($auth);
$config->setNetwork($network);
$config->setStartUp($startUp);

$homeList = new HomeItemList ;

$homeList-->

echo json_encode($config,JSON_PRETTY_PRINT);


echo json_encode($homeList,JSON_PRETTY_PRINT);
?>