$('document').ready(function(){

	

	var cmb_sucursal = $("#cmb_sucursal").val();
	var cmb_producto = $("#cmb_marca").val();
	var cmb_tipo = $("#cmb_tipo").val();

	console.log( cmb_sucursal,cmb_producto,cmb_tipo);


	$.ajax({
		contentType: "application/json",
		data : {"sucursal_id":cmb_sucursal ,
				"producto_id":cmb_producto,
				"tipo_id": cmb_tipo,},
		type:"get",
		url : "/producto/filtrocriterio/",
		dataType: "json"

	

	})
	.done(function(data){
		console.log("Testss");
		
		for(var i=0; i<data.length;i++)
		{
			console.log(data[i].producto_id+"xD");
		}
	})
	.fail(function(data){
		console.log("falla1");
		console.log(data);
	
	});





});
