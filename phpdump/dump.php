<?php
$request_method = $_SERVER['REQUEST_METHOD'];
$dump_dir = 'mtg/';

switch($request_method) {
case 'GET':
    $basename = basename($_GET['file']);
    $dumpf = $dump_dir . $basename;
    if(!file_exists($dumpf)) {
        die('cya');
    }
    header('Content-Description: File Transfer');
    header('Content-Type: application/octet-stream');
    header('Content-Disposition: attachment; filename="' . $basename . '"');
    header('Expires: 0');
    header('Cache-Control: must-revalidate');
    header('Pragma: public');
    header('Content-Length: ' . filesize($dumpf));
    readfile($dumpf);
    break;
case 'POST':
    $dumpf = $dump_dir . basename($_FILES['file']['name']);
    if(move_uploaded_file($_FILES['file']['tmp_name'], $dumpf)) {
        echo('posted');
    }
    else {
        die('nope');
    }
    break;
default:
    // Invalid Request Method
    header('HTTP/1.0 405 Method Not Allowed');
    break;
}
?>