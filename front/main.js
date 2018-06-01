// 表の動的作成
function makeTable(url, items, id){
  // JSONデータ取得
  var xmlHttp;
  xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", url, false);
  xmlHttp.send(null);
  var json = xmlHttp.responseText;
  obj = JSON.parse(json);
  let data = obj;

  // 表作成
  var rows=[];
  var table = document.createElement("table");

  rows.push(table.insertRow(-1));
  for(j = 0; j < items.length; j++){
    cell=rows[0].insertCell(-1);
    cell.appendChild(document.createTextNode(items[j]));
    cell.style.backgroundColor = "#CCEEEE"; // ヘッダ行
  }

  // 表に2次元配列の要素を格納
  for(i = 0; i < data.length; i++){
    rows.push(table.insertRow(-1));
    for(j = 0; j < items.length; j++){
      cell=rows[i+1].insertCell(-1);
      cell.appendChild(document.createTextNode(data[i][items[j]]));
      // 背景色の設定
      cell.style.backgroundColor = "#CCEEFF"; // ヘッダ行以外
      //console.log(data[i][items[j]]);
    }
  }
  document.getElementById(id).appendChild(table);
}

//window.onload = function() {
//  _URL_ = "https://xcl28qicy7.execute-api.ap-northeast-1.amazonaws.com/check/responseHistory";
//  _Items_ = ["user", "date", "url", "status"];
//  _TableID_ = "table";
//
//  makeTable(_URL_, _Items_, _TableID_);
//};

