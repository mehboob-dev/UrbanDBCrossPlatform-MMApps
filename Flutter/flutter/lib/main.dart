import 'package:flutter/material.dart';
import 'package:async/async.dart';
import 'dart:async';
import 'package:http/http.dart' as http;
void main(){
  runApp(MaterialApp(
    home:HomePage(),
  ));
}
class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  var api="trydemo";
    var sheet="Sheet1";
  String getLink(){
    return "https://urbandb.mmapps.in/"+api+"/"+sheet;
  }
  Future<String> getData() async{
    
    final response = await http.get(Uri.encodeFull('https://urbandb.mmapps.in/'+api+'/'+sheet+'/getAllRows'),headers: {
      "api":"trydemo",
      "Accept":"application/json"
    });
  print(response.body);
  return "hello";

  }
  Future<String> getrow(rowindex) async{
    rowindex=rowindex+1;
    
    final response = await http.get(Uri.encodeFull('https://urbandb.mmapps.in/'+api+"/"+sheet+'/getRow/$rowindex'),headers: {
      "api":"trydemo",
      "Accept":"application/json"
    });
  print(response.body);
  return "hello";

  }
  Future<String> getcolumn(colindex) async{
    
    final response = await http.get(Uri.encodeFull('https://urbandb.mmapps.in/'+api+"/"+sheet+'/getColumn/$colindex'),headers: {
      "api":"trydemo",
      "Accept":"application/json"
    });
  print(response.body);
  return "hello";

  }
  Future<String> getcell(rowindex,colindex) async{
    
    final response = await http.get(Uri.encodeFull('https://urbandb.mmapps.in/'+api+"/"+sheet+'/getCell/$rowindex/$colindex'),headers: {
      "api":"trydemo",
      "Accept":"application/json"
    });
  print(response.body);
  return "hello";

  }
  Future<String> getHeader() async{
    
    final response = await http.get(Uri.encodeFull('https://urbandb.mmapps.in/'+api+'/'+sheet+'/getHeader'),headers: {
      "api":"trydemo",
      "Accept":"application/json"
    });
  print(response.body);
  return "hello";

  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(

        child: Column(
          children: [
            RaisedButton(child: Text('Get All rows'),onPressed: getData),
            RaisedButton(child: Text('Get row'),onPressed:()=> getrow(1)),
            RaisedButton(child: Text('Get Column'),onPressed:()=> getcolumn(1)),
            RaisedButton(child: Text('Get cell'),onPressed:()=> getcell(3,5)),
            RaisedButton(child: Text('Get Header'),onPressed: getHeader),
          
          ],
        ),
      ),
    );
  }
}