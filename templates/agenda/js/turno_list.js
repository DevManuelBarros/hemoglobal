<script type="text/javascript">
    $(document).ready(function(){
        $(".generar_mensaje").on("click",  mensaje_portapapeles);
        $(".enviar_email").on("click", enviar_email)
	});

    function mensaje_portapapeles(){
        var id_mensaje = $(this).text();
        $("#" + id_mensaje).select();
        document.execCommand("copy");
    }

    function enviar_email(){
        var id_email = $(this).text();
        var id_mensaje = id_email.replace("email_", "turno_");
        var id_paciente = id_email.replace("email_", "paciente_");

        email = $("#" + id_email).text();
        mensaje = $("#" + id_mensaje).val();
        paciente= $("#" + id_paciente).text();

        

        // Empezamos con la petición ajaz
        var request = $.ajax({
			type : "GET",
			url : "{% url 'agenda:enviar_email' %}",
			data : {"mensaje" : mensaje, "email" : email, "paciente" : paciente },
        });
        
        request.done(function(response){
			alert(response.valor);

		});



    }

</script>