const btnDelete = document.querySelectorAll('.btn-delete')
// console.log(btnDelete)

if (btnDelete) {
    const arrayBtn = Array.from(btnDelete);
    arrayBtn.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if (!confirm('Estás seguro de eliminar este contacto?')){
                e.preventDefault() // Si el confirm es falso entonces se cancela el evento click y no se envía la petición
            }
        })
    })
}