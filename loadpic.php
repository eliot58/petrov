<?php
header('Content-Type: text/html; charset=utf-8');
$order_id 				= urldecode(escapeshellcmd($_GET['order_id']));
$email 				= urldecode(escapeshellcmd($_GET['email']));
$type = urldecode(escapeshellcmd($_GET['type']));

include("config.php");

if($type == '1'):
    $s = 'О\\';
else:
    $s = 'П\\';
endif;

$query = "exec pg_add_report_for_order '". $s ."". $order_id ."', 100000110, '". $email ."'";

$result = mssql_query($query);

mssql_close($dbhandle);

echo $query;

?>

