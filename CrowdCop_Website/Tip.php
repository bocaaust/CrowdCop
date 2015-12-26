

<!--Tip-->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html><head>
<title>Tip</title>

<meta name='Generator' content='Touch Forms for iPhone and iPad v5.30.1'>
<meta name="keywords" content="">
<meta name="description" content="">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/> 
<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js" type="text/javascript"></script>
<script src=Tip/jquery-1.7.2.min.js></script>

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
{$form9 = nl2br(strip_tags($_REQUEST['form9']));
$form3 = strip_tags($_REQUEST['form3']);
$form4 = strip_tags($_REQUEST['form4']);
$form5 = strip_tags($_REQUEST['form5']);

$headers="From:tips@crowd-cop.com\r\nContent-type:text/html\r\n";
$subject = 'Feedback from Tip';
mail('tips@crowd-cop.com', $subject, '<html><body>'.$form9.'<p><b>Date</b><p>'.$form3.'<p><b>Location</b><p>'.$form4.'<p><b>PayPal Username (Compensation for Successful Tips</b><p>'.$form5.'<p>', $headers);}

?>



<link href='http://fonts.googleapis.com/css?family=Actor|' rel='stylesheet' type='text/css'>
<style type=text/css>


.tab {text-indent:40px;}
.text0{position:absolute;left:335px;top:34px;z-index:35;font-size:28px;color:#4f4c4c;width:487px;height:47px;font-family:"Arial";padding:10px;border-style:none;border-width:0px;text-align:left;border-radius:0px;-moz-border-radius:0px;fixed:0;box-shadow: 0px 0px 0.000000px #000000;shadowOpacity:0.000000;shadowRadius:0.000000;shadowOffSetY:0;textAlpha:1.000000;indentFlag:0;text-indent:0px;}.text0 a:link {text-decoration: none; color: #4f4c4c;}.text0 a:visited {text-decoration: none; color: #4f4c4c;formType:;formTag:-99;formOptionTag:-99;formRequiredFlag:0;}
.text1{position:absolute;background-color:#FFFFFF;left:339px;top:79px;z-index:36;font-size:14px;color:#4f4c4c;width:560px;height:200px;font-family:"Actor";padding:0px;border-style:solid;border-width:1px;text-align:left;border-radius:0px;-moz-border-radius:0px;fixed:0;shadowOpacity:0.000000;shadowRadius:0.000000;shadowOffSetY:0;textAlpha:1.000000;indentFlag:0;text-indent:0px;}.text1 a:link {text-decoration: none; color: #4f4c4c;}.text1 a:visited {text-decoration: none; color: #4f4c4c;formType:textarea;formName:-99;formOptionTag:-99;formRequiredFlag:0;}
.text2{position:absolute;left:77px;top:369px;z-index:37;font-size:14px;color:#4f4c4c;width:180px;height:20px;font-family:"Actor";padding:10px;border-style:none;border-width:0px;text-align:left;border-radius:0px;-moz-border-radius:0px;fixed:0;box-shadow: 0px 0px 0.000000px #000000;shadowOpacity:0.000000;shadowRadius:0.000000;shadowOffSetY:0;textAlpha:1.000000;indentFlag:0;text-indent:0px;}.text2 a:link {text-decoration: none; color: #4f4c4c;}.text2 a:visited {text-decoration: none; color: #4f4c4c;formType:textLabel;formTag:1;formOptionTag:-99;formRequiredFlag:0;}
.text3{position:absolute;left:22px;top:399px;z-index:38;font-size:20px;color:#4f4c4c;width:90px;height:20px;font-family:"Actor";padding:10px;border-style:none;border-width:0px;text-align:right;border-radius:0px;-moz-border-radius:0px;fixed:0;box-shadow: 0px 0px 0.000000px #000000;shadowOpacity:0.000000;shadowRadius:0.000000;shadowOffSetY:0;textAlpha:1.000000;indentFlag:0;text-indent:0px;}.text3 a:link {text-decoration: none; color: #4f4c4c;}.text3 a:visited {text-decoration: none; color: #4f4c4c;formType:textLabel;formTag:1;formOptionTag:-22;formRequiredFlag:0;}
.text4{position:absolute;background-color:#FFFFFF;left:133px;top:402px;z-index:39;font-size:20px;color:#4f4c4c;width:104px;height:40px;font-family:"Futura";padding:0px;border-style:solid;border-width:1px;text-align:center;border-radius:0px;-moz-border-radius:0px;fixed:0;shadowOpacity:0.000000;shadowRadius:0.000000;shadowOffSetY:0;textAlpha:1.000000;indentFlag:0;text-indent:0px;}.text4 a:link {text-decoration: none; color: #4f4c4c;}.text4 a:visited {text-decoration: none; color: #4f4c4c;formType:text;formName:1;formOptionTag:-22;formRequiredFlag:0;}
.text5{position:absolute;left:102px;top:455px;z-index:41;font-size:20px;background-image:url(Tip/submit.png);background-repeat:	no-repeat;background-color:#FFFFFF;color:#000000;width:100px;height:25px;font-family:"Arial";padding:10px;border-style:solid;border-width:1px;text-align:center;border-radius:0px;-moz-border-radius:0px;fixed:0;opacity:1.000000;filter:alpha(opacity=100.000000);box-shadow: 0px 0px 0.000000px #000000;shadowOpacity:0.000000;shadowRadius:0.000000;shadowOffSetY:0;textAlpha:1.000000;indentFlag:0;text-indent:0px;formType:submit;formTag:2;formOptionTag:3;}
.submitButton{position:absolute;left:102px;top:455px;z-index:41;width:120px;height:45px;background-image:url(Tip/submit.png);background-repeat:no-repeat;text-indent:-999em;border:0;padding:0;margin:0;}
.text6{position:absolute;left:338px;top:287px;z-index:42;font-size:16px;color:#4f4c4c;width:280px;height:20px;font-family:"Arial";padding:10px;border-style:none;border-width:0px;text-align:left;border-radius:0px;-moz-border-radius:0px;fixed:0;box-shadow: 0px 0px 0.000000px #000000;shadowOpacity:0.000000;shadowRadius:0.000000;shadowOffSetY:0;textAlpha:1.000000;indentFlag:0;text-indent:0px;}.text6 a:link {text-decoration: none; color: #4f4c4c;}.text6 a:visited {text-decoration: none; color: #4f4c4c;formType:textLabel;formTag:3;formOptionTag:-99;formRequiredFlag:0;}
.text7{position:absolute;background-color:#FFFFFF;left:378px;top:332px;z-index:43;font-size:16px;color:#4f4c4c;width:300px;height:40px;font-family:"Actor";padding:0px;border-style:solid;border-width:1px;text-align:left;border-radius:0px;-moz-border-radius:0px;fixed:0;shadowOpacity:0.000000;shadowRadius:0.000000;shadowOffSetY:0;textAlpha:1.000000;indentFlag:0;text-indent:0px;}.text7 a:link {text-decoration: none; color: #4f4c4c;}.text7 a:visited {text-decoration: none; color: #4f4c4c;formType:text;formName:3;formOptionTag:-99;formRequiredFlag:0;}
.text8{position:absolute;left:337px;top:383px;z-index:44;font-size:16px;color:#4f4c4c;width:280px;height:20px;font-family:"Arial";padding:10px;border-style:none;border-width:0px;text-align:left;border-radius:0px;-moz-border-radius:0px;fixed:0;box-shadow: 0px 0px 0.000000px #000000;shadowOpacity:0.000000;shadowRadius:0.000000;shadowOffSetY:0;textAlpha:1.000000;indentFlag:0;text-indent:0px;}.text8 a:link {text-decoration: none; color: #4f4c4c;}.text8 a:visited {text-decoration: none; color: #4f4c4c;formType:textLabel;formTag:4;formOptionTag:-99;formRequiredFlag:0;}
.text9{position:absolute;background-color:#FFFFFF;left:377px;top:428px;z-index:45;font-size:16px;color:#4f4c4c;width:300px;height:40px;font-family:"Actor";padding:0px;border-style:solid;border-width:1px;text-align:left;border-radius:0px;-moz-border-radius:0px;fixed:0;shadowOpacity:0.000000;shadowRadius:0.000000;shadowOffSetY:0;textAlpha:1.000000;indentFlag:0;text-indent:0px;}.text9 a:link {text-decoration: none; color: #4f4c4c;}.text9 a:visited {text-decoration: none; color: #4f4c4c;formType:text;formName:4;formOptionTag:-99;formRequiredFlag:0;}
.text10{position:absolute;left:340px;top:476px;z-index:46;font-size:16px;color:#4f4c4c;width:400px;height:47px;font-family:"Arial";padding:10px;border-style:none;border-width:0px;text-align:left;border-radius:0px;-moz-border-radius:0px;fixed:0;box-shadow: 0px 0px 0.000000px #000000;shadowOpacity:0.000000;shadowRadius:0.000000;shadowOffSetY:0;textAlpha:1.000000;indentFlag:0;text-indent:0px;}.text10 a:link {text-decoration: none; color: #4f4c4c;}.text10 a:visited {text-decoration: none; color: #4f4c4c;formType:textLabel;formTag:5;formOptionTag:-99;formRequiredFlag:0;}
.text11{position:absolute;background-color:#FFFFFF;left:380px;top:522px;z-index:47;font-size:16px;color:#4f4c4c;width:300px;height:40px;font-family:"Actor";padding:0px;border-style:solid;border-width:1px;text-align:left;border-radius:0px;-moz-border-radius:0px;fixed:0;shadowOpacity:0.000000;shadowRadius:0.000000;shadowOffSetY:0;textAlpha:1.000000;indentFlag:0;text-indent:0px;}.text11 a:link {text-decoration: none; color: #4f4c4c;}.text11 a:visited {text-decoration: none; color: #4f4c4c;formType:text;formName:5;formOptionTag:-11;formRequiredFlag:0;}
.image0{position:absolute;left:10px;top:50px;z-index:40;background:transparent url("Tip/image0.PNG");imagename:image0;imagetype:PNG;width:320px;height:320px;border-style:none;border-width:1px;fixed:0;box-shadow:0px 0px 0.000000px #000000;shadowOpacity:0.000000;shadowRadius:0.000000;shadowOffSetY:0;imageAlpha:1.000000;display:inline;background:transparent url("Tip/image0.PNG");retina:1;slideShowNumber:-99;}
table, td, th{border:0px solid black; padding:0px;text-align:left;vertical-align:top;}



@media(-webkit-min-device-pixel-ratio: 2) {.image0{position:absolute;background-size:320px 320px !important;z-index:41;background:lightgrey url("Tip/image0@2x.PNG");}.submitButton{position:absolute;left:102px;top:455px;z-index:41;background-size:120px 45px !important;background-image:url(Tip/submit@2x.png);background-repeat:no-repeat;text-indent:-999em;border:0;padding:0;margin:0;}
}
</style></head>

<body bgcolor=lightgrey>
<div id=content><form name=Tip action=Tip.php onsubmit="return validateForm();" method=post>

<div class=text0>Please Enter Your Anonymous Tip</div>
<textarea class=text1 cols=56 rows=20 name=form9></textarea>
<div class=text2>Make sure you're human </div>
<div class=text3><?echo"$questionString";?></div>
<input class=text4 type="text" name=form1>
<input class=submitButton type="submit" name=form6>
<div class=text6>Date</div>
<input class=text7 type="text" name=form3>
<div class=text8>Location</div>
<input class=text9 type="text" name=form4>
<div class=text10>PayPal Username (Compensation for Successful Tips</div>
<input class=text11 type="text" name=form5>

<div class=image0 title=""></div>


<input type="hidden" name=email value="email"></form>

</div></body></html>