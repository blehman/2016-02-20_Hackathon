var button = d3.select('#buzz');
button.on('click',function(event){
    var hashtag = d3.select('#hashtag')[0][0].value;
    console.log(hashtag[0][0].value)
    var startDate = d3.select('#startDate')[0][0].value.replace(/[-]/g,'')+'0000';
    console.log(startDate)
    var endDate = d3.select('#endDate')[0][0].value.replace(/[-]/g,'')+'0000';
    console.log(endDate)
    var json_url = 'http://127.0.0.1:9090/get_data/'+hashtag+'/'+startDate+'/'+endDate+'/';
    d3.json(json_url,function(data){
        console.log('DATA:')
        console.log(data)
        // Check for the various File API support.
        //if (window.File && window.FileReader && window.FileList && window.Blob) {
        //  alert('Great success! All the File APIs are supported.');
        //  var selectedFile = document.getElementById('input').files[0];
        //  console.log(typeof(selectedFile))
        //} else {
        //  alert('The File APIs are not fully supported in this browser.');
        //}
    })
    var control_group = d3.select('#controlFile')[0][0].value
    console.log(control_group)
})

