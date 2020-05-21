async function getData(){
    try{
      search = document.getElementById("Search").value;
      let response = await fetch(`http://www.omdbapi.com/?s=${search}&apikey=cea8a076`);
      let result = await response.json();
      console.log(result);
      displayMovies(result);
   }catch(e){
       console.log(e);
   }
 }

 function displayMovies(data){
    let str = '';
    for(let movie of data.Search){
      str +=`
        <div class="col-md-3">
          <div class="card card-body bg-light text-center">
            <img class="card-img-top" src="${movie.Poster}">
            <h2>${movie.Title}</h2>
            <a onclick="movieSelected('${movie.imdbID}')" class="btn btn-primary href="#">Movie Details</a>
          </div>
        </div>
        
      `;
      
    }
    document.getElementById("movies").innerHTML = str;
 }

 function movieSelected(id){
   sessionStorage.setItem('movieID', id);
   window.location('/movie');
   return false;
 }

 async function getMovie(){
  try{
   let movieID = sessionStorage.getItem('movieID');
   let response = await fetch(`http://www.omdbapi.com/?i=${movieID}&apikey=cea8a076`);
   let movie = await response.json();
   console.log(movie);
   let str = `
    <div class="row">
      <div class="col-md-4">
        <img src="${movie.Poster}" class="thumbnail"> 
      </div
      <div class="col-md-8">
        <div class="card-body">
          <h2 class="card-title">${movie.Title}</h2>
          <ul class="list-group list-group-flush">
            <li class="list-group-item"><strong>Genre:</strong> ${movie.Genre}</li>
            <li class="list-group-item"><strong>Released:</strong> ${movie.Released}</li>
            <li class="list-group-item"><strong>Rated:</strong> ${movie.Rated}</li>
            <li class="list-group-item"><strong>imdbRating:</strong> ${movie.imdbRating}</li>
            <li class="list-group-item"><strong>Director:</strong> ${movie.Director}</li>
            <li class="list-group-item"><strong>Writer:</strong> ${movie.Writer}</li>
            <li class="list-group-item"><strong>Actors:</strong> ${movie.Actors}</li>
          </ul>
        </div>
      </div>
      </div>
    </div>
    <div class="row">
      <div class="card">
        <h3>Plot<h3>
          ${movie.Plot}
      </div>
    </div>
   `;
   document.getElementById("movie").innerHTML = str;

  }catch(e){
    console.log(e);
  }
}