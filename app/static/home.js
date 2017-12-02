function deleteFile(fileId, fileName) {
	if (confirm('Are you sure you want to delete ' + fileName + '?')) {
		$.ajax({
		    url: '/file/' + fileId,
		    type: 'DELETE',
		    success: function(result) {
		        location.reload();
		    }
		});
	}
}

$(document).ready(function(){
	$.get(
		'/file',
		function(data, status) {
			var fileArray = JSON.parse(data)['response']['files'];
			fileArray.forEach(function(element, index) {
				var link = $(`
					<div class="col-md-2">
						<figure class="figure">
							<a href="${element['path']}" target="_blank">
								<img src="https://n6-img-fp.akamaized.net/free-icon/file_318-143322.jpg?size=75c&ext=jpg" class="figure-img img-fluid rounded" alt="File">
							</a>
							<figcaption class="figure-caption">${element['file_name']}</figcaption>
						</figure>
						<button type="button" class="btn btn-danger" onclick="deleteFile(${element['id']}, '${element['file_name']}')">Delete</button>
					</div>
				`);
				$('#file_display').append(link);
			});
		}
	);
});
