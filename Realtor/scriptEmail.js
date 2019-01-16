function sendEmails() {
  var app = SpreadsheetApp.getActiveSpreadsheet();
  
  var res = app.getSheetByName("Pesquisador");
  var publ = app.getSheetByName("Publicacao");
  var target = app.getSheetByName("Alvo de Publicacao");
  
  var dataRes = res.getRange("A:D").getValues();
  var dataPubl = publ.getRange("A:E").getValues();
  var dataTarget = target.getRange("A:H").getValues();
  
  for(var i in dataPubl){
    if(i===0) continue;
    
    var publication = dataPubl[i];
    var nameAuthor = publication[0];
    var title = publication[1];
    var nameTarget = publication[3];
    
    var authors = dataRes.filter(function(x){
      if(nameAuthor.split("\n").indexOf(x[0]) > -1)
        return true;
    });
    
    var target = dataTarget.filter(function(x){
      if(nameTarget == x[1])
        return true;
    });
    
    if(target[0]){
      var listMonth = ["January","February","March","May","June","July","August","September","October","November","December"];
      var deadLinePaper = new Date(target[0][3]);
      var cont = 0
      for(var i in listMonth){
     if(i in deadLinePaper){
         var month = cont+1;
         if(month < 10){
             deadLinePaper.replace(i, "0"+month+"/");
         }
         else{
             deadLinePaper.replace(i+" ", month+"/");
         }
     }
     cont = cont + 1
      }
      deadLinePaper.replace(", ", "/")
      var daysPaper = Math.floor((new Date() - deadLinePaper)/1000/60/60/24)*-1;
      var deadLineAbstract = new Date(target[0][3]);
      cont = 0;
      for(var i in listMonth){
          if(i in deadLineAbstract){
            var month = cont+1;
            if(month < 10){
              deadLineAbstract.replace(i, "0"+month+"/");
            }
            else{
                deadLineAbstract.replace(i+" ", month+"/");
            }
          }
        cont = cont + 1
      }
      var daysAbstract = Math.floor((new Date() - deadLineAbstract)/1000/60/60/24)*-1;
      
      for(var author in authors){
        var message = "";
        var subject = "";
          
        if(daysAbstract<=3){
          message = "Dear "+authors[author][0]+", this is a "+"daily"+" notice for the submission of the abstract of your research entitled "+ title +"."+ days+" left";
          subject = "DAILY NOTICE";
        }
        else{
          if((daysAbstract-3)%7 === 0){
            message = "Dear "+authors[author][0]+", this is a "+"weekly"+" notice for the submission of the abstract of your research entitled "+ title +"."+ days+" left";
            subject = "WEEKLY NOTICE";
          }
          else{
            if(daysAbstract==-1){
              mensage = "Dear "+authors[author][0]+", the time for the submission of the abstract of your research entitled "+ title +" has expired. You have 14 days to inform that you have sent the project.";
              subject = "WARNING OF EXPIRATION";
            }
            else{
              if(daysAbstract==-14){
                mensage = "Dear "+authors[author][0]+", this is the last warning for the expiration of the research entitled "+ title +". You will not receive any notice on this particular research.";
                subject = "LAST WARNING OF EXPIRATION";
              }
            }
          }
        }
        if(daysPaper<=3){
          message = "Dear "+authors[author][0]+", this is a "+"daily"+" notice for the submission of your research entitled "+ title +"."+ days+" left";
          subject = "DAILY NOTICE";
        }
        else{
          if((daysPaper-3)%7 === 0){
            message = "Dear "+authors[author][0]+", this is a "+"weekly"+" notice for the submission of your research entitled "+ title +"."+ days+" left";
            subject = "WEEKLY NOTICE";
          }
          else{
            if(daysPaper==-1){
              mensage = "Dear "+authors[author][0]+", the time for the submission of your research entitled "+ title +" has expired. You have 14 days to inform that you have sent the project.";
              subject = "WARNING OF EXPIRATION";
            }
            else{
              if(daysPaper==-14){
                mensage = "Dear "+authors[author][0]+", this is the last warning for the expiration of the research entitled "+ title +". You will not receive any notice on this particular research.";
                subject = "LAST WARNING OF EXPIRATION";
              }
            }
          }
        }
        

        if(message){
          MailApp.sendEmail(authors[author][1], subject , message);
        }
      }
    }
    
  }
  for(i in dataRes){
    if(i===0) continue;
    
  }
  for(i in dataTarget){
    if(i===0) continue;
  }
}