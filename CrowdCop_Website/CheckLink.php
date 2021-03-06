<?php
//needs to pull test link from database
        if (isDomainAvailible('http://www.publicdomainpictures.net/pictures/40000/velka/red-bike.jpg'))
       {
               $var = 'http://www.publicdomainpictures.net/pictures/40000/velka/red-bike.jpg';
       }
       else
       {
               $var = 'http://crowd-cop.com/img/Default_Image.png';
       }

       //returns true, if domain is availible, false if not
       function isDomainAvailible($domain)
       {
               //check, if a valid url is provided
               if(!filter_var($domain, FILTER_VALIDATE_URL))
               {
                       return false;
               }

               //initialize curl
               $curlInit = curl_init($domain);
               curl_setopt($curlInit,CURLOPT_CONNECTTIMEOUT,10);
               curl_setopt($curlInit,CURLOPT_HEADER,true);
               curl_setopt($curlInit,CURLOPT_NOBODY,true);
               curl_setopt($curlInit,CURLOPT_RETURNTRANSFER,true);

               //get answer
               $response = curl_exec($curlInit);

               curl_close($curlInit);

               if ($response) return true;

               return false;
       }
?>