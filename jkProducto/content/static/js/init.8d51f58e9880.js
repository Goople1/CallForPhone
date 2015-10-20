$('document').ready(function(){

	

	var cmb_sucursal = $("#cmb_sucursal").val();
	var cmb_producto = $("#cmb_marca").val();
	var cmb_tipo = $("#cmb_tipo").val();

	console.log( cmb_sucursal,cmb_producto,cmb_tipo);


	$.ajax({

		data : {"sucursal_id":cmb_sucursal ,
				"producto_id":cmb_producto,
				"tipo_id": cmb_tipo,},
		type:"get",
		url : "/producto/filtrocriterio/",

	

	})
	.done(function(data){

		console.log(data);

	})

	.fail(function(data){

		console.log(data);

	});





});
