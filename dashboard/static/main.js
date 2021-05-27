console.log('hello world')

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')
const url = window.location.href


modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click',()=>{
        const pk = modalBtn.getAttribute('data-pk')
        const name = modalBtn.getAttribute('data-quiz')
        const numOfQuestions = modalBtn.getAttribute('data-questions')
        const time = modalBtn.getAttribute('data-time')
        console.log(name)
        modalBody.innerHTML = `
          <div class="h5 mb-3"> Are you sure you want to begin "<b>${name}</b>"?</div>
           <div class="text-muted">
                <ul>
                    <li> number of questions :<b>${numOfQuestions}</b> </li>
                    <li> time :<b>${time}</b> </li>
                </ul>
           </div>
         `
    startBtn.addEventListener('click',()=>{
         window.location.href = url+pk
    })

}))