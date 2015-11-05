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

	var result = []
	      for (var i = 0 ; i < data.length ; i ++){
	
	        console.log("data" , data[i].producto.color);

	        result.push(to_show(data[i]));

      }


      console.log("result  : ", result)

      $("#result").append(result);
	})

	.fail(function(data){

		console.log(data);

	});





  function to_show(data){

   article =  $("<article/>",{"class":"grid-item on async-photo"});
   		header = $("<header/>",{"class" : "grid-item-header"})
    		h2 = $("<h2/>" , {"class" : "grid-item-title"})
        		h2.text(data.producto.marca.nombre);
        			p = $("<p/>")
        			p.text(data.producto.codigo + "  " + data.producto.color + "  " + data.producto.tipo_producto.nombre );

        			p.appendTo(h2);
        		h2.appendTo(header);

        header.appendTo(article);

        div_multimedia = $("<div/>", { "class" : "multimedia-canvas"});
        	figure = $("<figure/>" , {"class":"image-canvas"});
		        img  = $("<img/>" , {"src" : data.producto.imagen,"height": "140px"});
	       		img.appendTo(figure);
	       	figure.appendTo(div_multimedia);
   		div_multimedia.appendTo(article);


   		div_content = $(" <div class='grid-item-content'>"+
   							"<p style = 'margin:0px;'>  Sucursal: "+ data.sucursal.nombre+"</p>"+	
   							"<p style = 'margin:0px;''>  Direccion: "+ data.sucursal.direccion +" "+ data.sucursal.departamento+"</p>"+
   							//"<p>Telefono: "+ data.sucursal.telefono+"<p/>"+
   							//"<p>Cel: "+ data.sucursal.celular+"<p/>"+

						   " <p>Stock"+
						   "<span class='grid-item-price atm-equipo-precio' >"+
           					data.stock+" </span></p></div>");


   		div_content.appendTo(article);




    return article;
}






});
