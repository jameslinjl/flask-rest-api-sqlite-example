$(document).ready(function(){
	$.get(
		'/file',
		function(data, status) {
			var file_array = JSON.parse(data)['response']['files'];
			file_array.forEach(function(element, index) {
				var link = $('<a></a>');
				link.text(element['file_name']);
				link.attr('target', '_blank');
				link.attr('href', element['path']);
				$('#file_display').append(link, '<br>');
			});
		}
	);
}