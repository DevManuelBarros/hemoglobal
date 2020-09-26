<script type="text/javascript">
	$(document).ready(function(){
		$("#btn_cambiar_estado_turno").on("click", cambiar_estado_turno);	
	});


	function cambiar_estado_turno(){
		var turno_pk = $("#turno_id").text();
		var request = $.ajax({
			type : "GET",
			url : "{% url 'agenda:cambiar_estado_turno' %}",
			data : {"pk" : turno_pk },
		});

		request.done(function(response){
			$("#estado").text(response.valor);

		});
	}

</script>
