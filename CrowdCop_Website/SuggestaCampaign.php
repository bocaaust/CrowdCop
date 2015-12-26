<!--Suggest a Campaign-->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html><head>
<title>Suggest a Campaign</title>
<meta name='viewport' content='width=740'>
<meta name='Generator' content='Touch Forms for iPhone and iPad v5.30.1'>
<meta name="keywords" content="">
<meta name="description" content="">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/> 
<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js" type="text/javascript"></script>
<script src=SuggestaCampaign/jquery-1.7.2.min.js></script>

<!--Touch Forms Custom Header Code:45-->
<link href="css/bootstrap.css" rel="stylesheet" type="text/css">
<nav>
  <div class="container"> 
    
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>
      <a class="navbar-brand" href="/index.html">CrowdCop</a></div>
    
    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse">
      <ul class="nav navbar-nav">
        <li class="active"><a href="/Tip.php">Submit a Tip <span class="sr-only">(current)</span></a> </li>
        <li><a href="#">Dashboard</a> </li>
        <li class="dropdown"> <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">My CrowdCop<span class="caret"></span></a>
          <ul class="dropdown-menu" role="menu">
            <li><a href="#">Profile</a> </li>
            <li><a href="#">History</a> </li>
            <li><a href="#">Nearby Campaigns</a> </li>
            <li class="divider"></li>
            <li><a href="/SuggestaCampaign.php">Suggest a Campaign</a> </li>
          </ul>
        </li>
      </ul>
      <form class="navbar-form navbar-right" role="search">
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Search">
        </div>
        <button type="submit" class="btn btn-default">Submit</button>
      </form>
      <ul class="nav navbar-nav navbar-right hidden-sm">
        <li><a href="#">Random</a> </li>
        <li class="dropdown"> <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">About <span class="caret"></span></a>
          <ul class="dropdown-menu" role="menu">
            <li><a href="#">Creators</a> </li>
            <li><a href="#">Press</a> </li>
            <li class="divider"></li>
            <li><a href="#">RCOS</a> </li>
          </ul>
        </li>
      </ul>
    </div>
    <!-- /.navbar-collapse --> 
  </div>
  <!-- /.container-fluid --> 
</nav>
<?php
$firstNumber=rand(0,9);
$secondNumber=rand(0,9);
$answerNumber=$firstNumber+$secondNumber;
$questionString="$firstNumber + $secondNumber=";
if (isset($_REQUEST['email']))
{$form0 = strip_tags($_REQUEST['form0']);
$form2 = nl2br(strip_tags($_REQUEST['form2']));

$headers="From:bocaaust@gmail.com\r\nContent-type:text/html\r\n";
$subject = 'Suggest a Campaign';
mail('campaigns@crowd-cop.com', $subject, '<html><body><b>Suggest a Campaign</b><p>'.$form0.'<p><b>Additional Info</b><p>'.$form2.'<p>', $headers);
echo"<meta http-equiv='refresh' content='0; url=http://www.crowd-cop.com'>";}
?>

<SCRIPT LANGUAGE='JavaScript'>
function validateEmail(email)
{ var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(".+"))@(([[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
return re.test(email);
}

function validateForm()
{
//FORMREDIRECTURLhttp://www.crowd-cop.comFORMREDIRECTURLEND
//FORMSUBMITSubmitFORMSUBMITEND
//FORMEMAILVERIFICATIONEmail address entered is invalid, please check and submit again.FORMEMAILVERIFICATIONEND
//FORMBOTCHECKERMSGBot checker answer incorrect, please try again.FORMBOTCHECKERMSGEND
var showRequiredAlert=0;
var x;
var showEmailAlert=0;
var emailX;
var validateFlag=true;

var showBotCheckerAlert=0;
var botCheckerValue;
if (showRequiredAlert==1)
{
alert('Required form fields are incomplete, please complete and submit again.');
//FORMMISSINGMSGRequired form fields are incomplete, please complete and submit again.FORMMISSINGMSGEND
return false;
}
if (showEmailAlert==1)
{
alert('Email address entered is invalid, please check and submit again.');
return false;
}
if (showBotCheckerAlert==1)
{
alert('Bot checker answer incorrect, please try again.');
return false;
}
else{
alert('Thank you for submitting a Campaign');
//FORMRESPONSEMSGThank you for submitting a CampaignFORMRESPONSEMSGEND
return true;
}
}
</SCRIPT>

<link href='http://fonts.googleapis.com/css?family=Actor|' rel='stylesheet' type='text/css'>
<style type=text/css>
#content{position:relative;width:740px;margin-left:auto;margin-right:auto;}


.tab {text-indent:40px;}
.text0{position:absolute;left:420px;top:160px;z-index:35;font-size:18px;color:#4f4c4c;width:200px;height:20px;font-family:"Arial";padding:10px;border-style:none;border-width:0px;text-align:left;border-radius:0px;-moz-border-radius:0px;fixed:0;box-shadow: 0px 0px 0.000000px #000000;shadowOpacity:0.000000;shadowRadius:0.000000;shadowOffSetY:0;textAlpha:1.000000;indentFlag:0;text-indent:0px;}.text0 a:link {text-decoration: none; color: #4f4c4c;}.text0 a:visited {text-decoration: none; color: #4f4c4c;formType:textLabel;formTag:0;formOptionTag:-99;formRequiredFlag:0;}
.text1{position:absolute;background-color:#FFFFFF;left:360px;top:220px;z-index:36;font-size:16px;color:#4f4c4c;width:300px;height:40px;font-family:"Actor";padding:0px;border-style:solid;border-width:1px;text-align:left;border-radius:0px;-moz-border-radius:0px;fixed:0;shadowOpacity:0.000000;shadowRadius:0.000000;shadowOffSetY:0;textAlpha:1.000000;indentFlag:0;text-indent:0px;}.text1 a:link {text-decoration: none; color: #4f4c4c;}.text1 a:visited {text-decoration: none; color: #4f4c4c;formType:text;formName:0;formOptionTag:-99;formRequiredFlag:0;}
.text2{position:absolute;left:439px;top:520px;z-index:37;font-size:18px;background-image:url(Tip/submit.png);background-repeat:	no-repeat;background-color:#FFFFFF;color:#808080;width:99px;height:25px;font-family:"Arial";padding:10px;border-style:solid;border-width:1px;text-align:center;border-radius:0px;-moz-border-radius:0px;fixed:0;opacity:1.000000;filter:alpha(opacity=100.000000);box-shadow: 0px 0px 0.000000px #000000;shadowOpacity:0.000000;shadowRadius:0.000000;shadowOffSetY:0;textAlpha:1.000000;indentFlag:0;text-indent:0px;formType:submit;formTag:1;formOptionTag:2;}
.submitButton{position:absolute;left:439px;top:520px;z-index:37;width:119px;height:45px;background-image:url(Tip/submit.png);background-repeat:no-repeat;text-indent:-999em;border:0;padding:0;margin:0;}
.text3{position:absolute;left:459px;top:260px;z-index:38;font-size:14px;color:#4f4c4c;width:118px;height:20px;font-family:"Arial";padding:10px;border-style:none;border-width:0px;text-align:left;border-radius:0px;-moz-border-radius:0px;fixed:0;box-shadow: 0px 0px 0.000000px #000000;shadowOpacity:0.000000;shadowRadius:0.000000;shadowOffSetY:0;textAlpha:1.000000;indentFlag:0;text-indent:0px;}.text3 a:link {text-decoration: none; color: #4f4c4c;}.text3 a:visited {text-decoration: none; color: #4f4c4c;formType:textLabel;formTag:2;formOptionTag:-99;formRequiredFlag:0;}
.text4{position:absolute;background-color:#FFFFFF;left:360px;top:300px;z-index:39;font-size:14px;color:#4f4c4c;width:300px;height:200px;font-family:"Actor";padding:0px;border-style:solid;border-width:1px;text-align:left;border-radius:0px;-moz-border-radius:0px;fixed:0;shadowOpacity:0.000000;shadowRadius:0.000000;shadowOffSetY:0;textAlpha:1.000000;indentFlag:0;text-indent:0px;}.text4 a:link {text-decoration: none; color: #4f4c4c;}.text4 a:visited {text-decoration: none; color: #4f4c4c;formType:textarea;formName:2;formOptionTag:-99;formRequiredFlag:0;}
table, td, th{border:0px solid black; padding:0px;text-align:left;vertical-align:top;}



@media(-webkit-min-device-pixel-ratio: 2) {.submitButton{position:absolute;left:439px;top:520px;z-index:37;background-size:119px 45px !important;background-image:url(SuggestaCampaign/submit@2x.png);background-repeat:no-repeat;text-indent:-999em;border:0;padding:0;margin:0;}
}
</style></head>

<body bgcolor=#FFFFFF>
<div id=content><form name=SuggestaCampaign action=SuggestaCampaign.php onsubmit="return validateForm();" method=post>

<div class=text0>Suggest a Campaign</div>
<input class=text1 type="text" name=form0>
<input class=submitButton type="submit" name=form3>
<div class=text3>Additional Info</div>
<textarea class=text4 cols=30 rows=20 name=form2></textarea>



<input type="hidden" name=email value="email"></form>

</div></body></html>