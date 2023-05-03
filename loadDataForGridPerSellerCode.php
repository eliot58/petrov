<?php
$s_code 						= urldecode(escapeshellcmd($_GET['s_code']));
$create_date_from 			= urldecode(escapeshellcmd($_GET['create_date_from']));
$create_date_to 				= urldecode(escapeshellcmd($_GET['create_date_to']));
$order_id_from 				= urldecode(escapeshellcmd($_GET['order_id_from']));
$order_id_to 					= urldecode(escapeshellcmd($_GET['order_id_to']));
$manufacture_date_from 	= urldecode(escapeshellcmd($_GET['manufacture_date_from']));
$manufacture_date_to 		= urldecode(escapeshellcmd($_GET['manufacture_date_to']));
$ready_date_from 			= urldecode(escapeshellcmd($_GET['ready_date_from']));
$ready_date_to 				= urldecode(escapeshellcmd($_GET['ready_date_to']));
$filter_select_state 			= urldecode(escapeshellcmd($_GET['filter_select_state']));
$jsoncallback 					= escapeshellcmd($_GET['jsoncallback']);

header("Access-Control-Allow-Origin: *");

include("config.php");

//declare the SQL statement that will query the database
$query = "
	SELECT
		wdi.order_date_create,
		wdi.order_name,
		wdi.date_start,
		wdi.date_end_plan,
		wdi.deliverytime,
		wdi.date_end_fact,
		wdi.state_name,
		wdi.items_qu,
		wdi.items_sqr,
		wdi.order_sm,
		wdi.sm_pay,
		wdi.sm_dolg,
		wdi.dop_data,
		wdi.dop_comment,
		wdi.No_dil,
		wdi.service_flag,
		wdi.idorder,
		wdi.prof_name,
		wdi.furn_name,
		wdi.sp_name
	FROM dbo.web_diler_info_new_lk wdi
	WHERE 	wdi.seller_code = '".  iconv("UTF-8", "windows-1251", $s_code)  ."' ";

if($create_date_from != "" && $create_date_to != "" ){
	$query = $query . " AND wdi.order_date_create BETWEEN CONVERT(datetime, '". iconv("UTF-8", "windows-1251", $create_date_from) ."', 120) AND  CONVERT(datetime, '". iconv("UTF-8", "windows-1251", $create_date_to) ."', 120) ";
}

if($order_id_from != ""){
	$query = $query . " AND (CASE WHEN ISNUMERIC(wdi.order_name)=1 THEN CAST(wdi.order_name AS INT) else -1 END)  >= ". iconv("UTF-8", "windows-1251", $order_id_from ) ." ";
}

if($order_id_to != ""){
	$query = $query . " AND (CASE WHEN ISNUMERIC(wdi.order_name)=1 THEN CAST(wdi.order_name AS INT) else -1 END) <= ". iconv("UTF-8", "windows-1251", $order_id_to ) ." ";
}

if($manufacture_date_from != "" && $manufacture_date_to != "" ){
	$query = $query . " AND wdi.date_start BETWEEN CONVERT(datetime, '". iconv("UTF-8", "windows-1251", $manufacture_date_from) ."', 120) AND  CONVERT(datetime, '". iconv("UTF-8", "windows-1251", $manufacture_date_to) ."', 120) ";
}

if($ready_date_from != "" && $ready_date_to != "" ){
	$query = $query . " AND wdi.date_end_plan BETWEEN CONVERT(datetime, '". iconv("UTF-8", "windows-1251", $ready_date_from) ."', 120) AND  CONVERT(datetime, '". iconv("UTF-8", "windows-1251", $ready_date_to) ."', 120) ";
}

if($filter_select_state != ""){
	$query = $query . " AND rtrim(ltrim(wdi.state_name)) = rtrim(ltrim('". iconv("UTF-8", "windows-1251", $filter_select_state ) ."')) ";
}

$query = $query . " ORDER BY wdi.order_date_create DESC";

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

echo $jsoncallback.'('.$jsonresult.')';

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
