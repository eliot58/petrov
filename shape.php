<?php
$order_id                               = urldecode(escapeshellcmd($_GET['order_id']));
$type = urldecode(escapeshellcmd($_GET['type']));

include("config.php");

if($type == '1'):
    $s = 'О\\';
else:
    $s = 'П\\';
endif;

//declare the SQL statement that will query the database
$query = "select seller_code from dbo.web_diler_info_new_lk where order_name = '". $s ."". $order_id ."' ";

//execute the SQL query and return records
$result = mssql_query($query);

$arrRes = array();

$numRows = mssql_num_rows($result);
if($numRows > 0){
	while($row = mssql_fetch_assoc($result)){
	  	$arrRes[] = $row;
	}
};

//close the connection
mssql_close($dbhandle);

$jsonresult =  json_encode(utf8_converter($arrRes));

echo $jsonresult;

function utf8_converter($array)
{
    array_walk_recursive($array, function(&$item, $key){
        if(!mb_detect_encoding($item, 'utf-8', true)){
                $item =  iconv("windows-1251", "UTF-8", $item);
        }
    });

    return $array;
}

?>

