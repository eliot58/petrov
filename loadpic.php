<?php
$order_id 				= urldecode(escapeshellcmd($_GET['order_id']));


include("config.php");



$query = "
select mp.picture,
    o.name as o_name,oi.numpos,s.name as p_name, fs.name as f_name,
    oi.sqr,oi.comment,
    oi.qu,case when oi.idconstructiontype=2 then 'ОП' when oi.idconstructiontype=3 then 'БП' end type_con,
oi.width,
oi.height,
case when exists(select * from orderitem where idproductiontype=106 and parentid=oi.idorderitem) then 'ОСП'
else 'О' end type_con1,
c1.name c1_name, c2.name c2_name,
(select dbo.at_concatstr(distinct name)  from orderitem  where Parentid=oi.idorderitem 
    and idproductiontype in (106,114))glasses
 from 
    orders o inner join
    orderitem oi  on oi.idorder=o.idorder and o.idorder=". iconv("UTF-8", "windows-1251", $order_id) ."
and isnull(oi.idmodel,0)<>0 and oi.hide is null
inner join
system s on oi.idprofsys=s.idsystem 
inner join 
system fs on oi.idfurnsys=fs.idsystem
inner join view_model m on m.idmodel = oi.idmodel and m.deleted is null
inner join view_modelpic mp on oi.idorderitem=mp.idorderitem and mp.typ=1
left join color c1 on c1.idcolor=oi.idcolorout
left join color c2 on c2.idcolor=oi.idcolorin";

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
