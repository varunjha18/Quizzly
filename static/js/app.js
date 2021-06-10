setTimeout(function() {
    mes = document.getElementById('message')
    console.log(mes)
    console.log('this function is working')

    $('#message').fadeOut('slow');
}, 5000)



update_details = document.getElementById('update_details')
view_details = document.getElementById('view_details')

update_profile_button = document.getElementById("update_profile_button");
update_details.style.display = 'none'


update_profile_button.addEventListener('click', () => {
    view_details.style.display = 'none';
    update_details.style.display = 'flex'
    update_profile_button.id = 'submit_updates';
    update_profile_button.innerHTML = 'Submit'
    submit_update_button = document.getElementById('submit_updates')
    submit_update_button.addEventListener('click', () => {
        view_details.style.display = 'flex';
        update_details.style.display = 'none';
        document.getElementById("update_profile_form").submit()

    })
})


submit_update_button = document.getElementById('submit_updates')
submit_update_button.addEventListener('click', () => {
    view_details.style.display = 'flex'
    update_details.style.display = 'none'


})