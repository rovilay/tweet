<!DOCTYPE html>
<html>
   <head>
    <meta charset="utf-8">
    <title>Tweeter</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <style>
      body {
        border: bold;
      }

      a {
          color: pink;
          font: comic sans;
      }
      h1, h3 {
          color: Red;
      }
    </style>
   </head>
  <body>
    <h1>Trending in {{s}} on {{date}}</h1>
    <h3> Where on Earth ID: {{woeid}}
    <table>
     <tr><th>Name</th>
      %for row in twitter_trends:
     <tr>
    
       <td><a href={{row[1]}}>{{row[0]}}</a></td>
   
     </tr>
    %end
    </table>
   </body>
</html>