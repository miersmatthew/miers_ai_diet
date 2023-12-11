function App() {
  return (
    <div className="app">
      <TitleSection />
      <GameSection />
      <WinCard />
      <LoseCard />
    </div>
  );
}

var disableGameSection;
class GameSection extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      disabled: false
    }
  }
  componentDidMount(){
    disableGameSection = () => {
      this.setState({ disabled: true });     
    };
  }
  render() {
    let selcard1,selcard2;
    if(gamemode==1){
      selcard1 = <SelectionCard selType='synonyms'/>;
      selcard2 = null;
    }else{
      selcard1 = <SelectionCard selType='synonyms'/>;
      selcard2 = <SelectionCard selType='antonyms'/>;
    }
    return (
      <div className={`game-section ${this.state.disabled ? 'disabled': null}`} disabled={this.state.disabled}>
        <GameBar />
        <TargetBar />
        <PathBar />
        <div className="selection-cards">
          {selcard1}
          {selcard2}
        </div>
      </div>
    );
  }
}

var titleChangeFunc;
class TitleSection extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      randomWord: ""
    }
  }
  componentDidMount(){
    titleChangeFunc = (word) => {
      this.setState({ randomWord: word});     
    };
  }
  render() {
    return (
      <div className="title-section">
        <p>6 Degrees of [{ this.state.randomWord }]</p>
      </div>
    );
  }
}

var updateMovesLeft;
var updateUndosLeft;
var updateGameName;
class GameBar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      mLeft: 0,
      uLeft: 0,
      gameName: 'synonyms'
    }
  }
  componentDidMount(){
    updateMovesLeft = (n) => {
      this.setState({ mLeft: n});     
    };
    updateUndosLeft = (n) => {
      this.setState({ uLeft: n});     
    };
    updateGameName = (gn) => {
      this.setState({ gameName: gn});     
    };
  }
  render() {
    return (
      <div className="game-bar">
        <div className="game-bar-left">
          <p>{ this.state.gameName } Game</p>
        </div>
        <div className="game-bar-right">
          <p>{ this.state.mLeft } moves left</p>
          <p>{ this.state.uLeft } undos left</p>
        </div>
      </div>
    );
  }
}

var currentWordUpdate;
var targetWordUpdate;
class TargetBar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      curWord: "",
      tarWord: ""
    }
  }
  componentDidMount(){
    currentWordUpdate = (w) => {
      this.setState({ curWord: w});     
    };
    targetWordUpdate = (w) => {
      this.setState({ tarWord: w});     
    };
  }
  render() {
    return (
      <div className="target-bar">
        <div className="target-bar-left">
          <p>Current: { this.state.curWord }</p>
        </div>
        <div className="target-bar-right">
          <p>Target: { this.state.tarWord }</p>
        </div>
      </div>
    );
  }
}

var pathSoFarUpdate;
class PathBar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      path: []
    }
  }
  componentDidMount(){
    pathSoFarUpdate = (p) => {
      this.setState({ path: p});     
    };
  }
  render() {
    return (
      <div className="path-bar">
        <div className="path-bar-left">
          <p>Path so Far: {this.state.path.map((p, i, arr) => {
            if (i + 1 === arr.length) {
              return p
            } else {
              return p+" > "
            }
          })}</p>
        </div>
        <div className="path-bar-right">
          <button onClick={() => undoLastWord()}>UNDO last move</button>
        </div>
      </div>
    );
  }
}

var updateSelectionList = {};
class SelectionCard extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      items: []
    }
  }
  componentDidMount(){
    updateSelectionList[this.props.selType] = (list) => {
      this.setState({ items: list});     
    };
  }
  render() {
    return (
      <div className="selection-card">
        <p>{this.props.selType}</p>
        {this.state.items.map((item) => (
          <button key={item} onClick={() => exploreWord(item)}>{item}</button>
        ))}
      </div>
    );
  }
}

var setWinComponent;
class WinCard extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      visible: false,
      path: []
    };
  }

  componentDidMount(){
    setWinComponent = (p) => {
      this.setState({ visible: true});   
      this.setState({ path: p});     
    };
  }

  routeChange=()=> {
    window.location.href=`mainpage.html`;
  }

  render() {
    return (
      <div className={`win-overlay ${this.state.visible ? 'visible': null}`}>
        <div className="win-card">
          <div className="end-card-name">
            <p>YOU WIN!</p>
          </div>
          <div className="end-card-path">
            <p>Path taken: {this.state.path.map((p, i, arr) => {
              if (i + 1 === arr.length) {
                return p
              } else {
                return p+" > "
              }
            })}</p>
          </div>
          <div className="end-card-options">
            <button onClick={this.routeChange} >Play Again</button>
          </div>
        </div>
      </div>
    );
  }
}

var setLoseComponent;
class LoseCard extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      visible: false,
      path: []
    };
  }

  routeChange=()=> {
    window.location.href=`mainpage.html`;
  }

  componentDidMount(){
    setLoseComponent = (p) => {
      this.setState({ visible: true});   
      this.setState({ path: p});     
    };
  }

  render() {
    return (
      <div className={`lose-overlay ${this.state.visible ? 'visible': null}`}>
        <div className="lose-card">
          <div className="end-card-name">
            <p>YOU LOSE!</p>
          </div>
          <div className="end-card-path">
            <p>Correct path: {this.state.path.map((p, i, arr) => {
              if (i + 1 === arr.length) {
                return p
              } else {
                return p+" > "
              }
            })}</p>
          </div>
          <div className="end-card-options">
            <button onClick={this.routeChange} >Play Again</button>
          </div>
        </div>
      </div>
    );
  }
}

//helper functions
function removeMatching(target, blacklist){
  var ret = target.filter( function( el ) {
    return blacklist.indexOf( el ) < 0;
  } );
  return ret;
}

function removeDupes(list){
  return list.filter((value, index) => list.indexOf(value) === index);
}

function chooseRandomWord(list){
  return list[Math.floor(Math.random()*list.length)];
}

//JQuery fujnctions
function getRandomWord() {
  /*const settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://wordsapiv1.p.rapidapi.com/words/?letterPattern=%5E%5Ba-z%5D%7B4%2C10%7D%24&hasDetails=synonyms%2Cantonyms%2Cdefinitions%2Cexamples&random=true",
    "method": "GET",
    "headers": {
      "X-RapidAPI-Key": "84abbd7514msha5595d42b7db3acp1c12dbjsn45aa7afe43e8",
      "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }
  };
  
  $.ajax(settings).done(function (response) {
    gameInfo.startWord = response.word;
    gameInfo.curWord = response.word;
    gameInfo.path = [response.word];
    getWordInfo(gameInfo.startWord);
    //hardcoded for now
    var steps = url.searchParams.get("moves")-1;
    getTargetWord(steps, [gameInfo.startWord], gameInfo.startWord)
  });*/

  var array = ["good", "new", "first", "last", "long", "great", "little", "own", "other", "old"];
  var word = array[Math.floor(Math.random() * array.length)];
  gameInfo.startWord = word;
  gameInfo.curWord = word;
  gameInfo.path = [word];
  getWordInfo(gameInfo.startWord);
  //hardcoded for now
  var steps = url.searchParams.get("moves")-1;
  getTargetWord(steps, [gameInfo.startWord], gameInfo.startWord);

}

function getWordInfo(word) {
  const settings = {
    "async": true,
    "crossDomain": true,
    "url": `https://api.api-ninjas.com/v1/thesaurus?word=${word}`,
    "method": "GET",
    "headers": {
      "X-Api-Key": "iZoHeWSYGXpxGlyjYTuM6w==AgB5UiS3v4Vp8C42"
    }
  };
  
  $.when(
    $.ajax(settings).done(function (response) {
      response.synonyms = removeDupes(response.synonyms);
      response.antonyms = removeDupes(response.antonyms);
      gameInfo.selectionList.synonyms = removeMatching(response.synonyms, [word]);
      gameInfo.selectionList.antonyms = removeMatching(response.antonyms, [word]);
      console.log(`DONE callback`);
    })).done(function(){
      console.log(`Explored: ${word}`);
      updateGameInfoDisplays();
    });
}

function getTargetWord(stepsRemaining, selectionPath, currentWord){
  stepsRemaining -= 1;
  const settings = {
    "async": true,
    "crossDomain": true,
    "url": `https://api.api-ninjas.com/v1/thesaurus?word=${currentWord}`,
    "method": "GET",
    "headers": {
      "X-Api-Key": "iZoHeWSYGXpxGlyjYTuM6w==AgB5UiS3v4Vp8C42"
    }
  };
  
  $.ajax(settings).done(function (response) {
    if (gamemode == 1){
      var possibleList = removeMatching(response.synonyms, selectionPath);
    }
    else{
      var possibleList = removeMatching(response.synonyms.concat(response.antonyms), selectionPath);
    }
    if(possibleList.length == 0){
      console.log(`selected word ${currentWord}`);
      gameInfo.tgtWord = currentWord;
      gameInfo.tgtPath = selectionPath;
      updateGameInfoDisplays();
    }
    else{
      var selection = chooseRandomWord(possibleList);
      selectionPath.push(selection);
      if(stepsRemaining>0){
        getTargetWord(stepsRemaining, selectionPath, selection);
      }
      else{
        console.log(`selected word ${selection}`);
        gameInfo.tgtWord = selection;
        gameInfo.tgtPath = selectionPath;
        updateGameInfoDisplays();
      }
    }
  });
}

//game setup
var url = new URL(window.location.href);
var gamemode = url.searchParams.get("gm");

var gameInfo = {
  gameName: "game name",
  movesLeft: url.searchParams.get("moves"),
  undosLeft: url.searchParams.get("moves"),
  startWord: "",
  curWord: "",
  tgtWord: "TARGET",
  tgtPath: [],
  path: [],
  selectionList: {
    synonyms: [],
    antonyms: []
  }
};

if (gamemode == 1) {
  gameInfo.gameName = 'Synonyms';
  updateSelectionList.antonyms=(w) => {
    return;     
  };
}
else{
  gameInfo.gameName = 'Synonyms and Antonyms';
}


//game functionality
var displayTimeout;
function updateGameInfoDisplays(){
  if(!(typeof displayTimeout === 'undefined')){
    clearTimeout(displayTimeout);
  }
  if (typeof titleChangeFunc === 'undefined' ||
      typeof updateMovesLeft === 'undefined' ||
      typeof updateUndosLeft === 'undefined' ||
      typeof currentWordUpdate === 'undefined' ||
      typeof targetWordUpdate === 'undefined' ||
      typeof pathSoFarUpdate === 'undefined' ||
      typeof updateSelectionList.synonyms === 'undefined' ) {
    displayTimeout = setTimeout(updateGameInfoDisplays, 100);
    console.log("timeout1");
    return;
  }
  else if (gamemode == 2 && typeof updateSelectionList.antonyms === 'undefined' ){
    displayTimeout = setTimeout(updateGameInfoDisplays, 100);
    console.log("timeout2");
    return;
  }
  titleChangeFunc(gameInfo.startWord);
  updateGameName(gameInfo.gameName);
  updateMovesLeft(gameInfo.movesLeft);
  updateUndosLeft(gameInfo.undosLeft);
  currentWordUpdate(gameInfo.curWord);
  targetWordUpdate(gameInfo.tgtWord);
  pathSoFarUpdate(gameInfo.path);
  updateSelectionList.synonyms(gameInfo.selectionList.synonyms);
  updateSelectionList.antonyms(gameInfo.selectionList.antonyms);
}

function exploreWord(wChoice){
  gameInfo.movesLeft -= 1;
  gameInfo.curWord = wChoice;
  gameInfo.path.push(wChoice);
  if (wChoice == gameInfo.tgtWord) {
    handleWin();
    return
  }
  if (gameInfo.movesLeft <= 0) {
    handleLose();
    return
  }
  getWordInfo(wChoice);
}

function undoLastWord(){
  if(gameInfo.path.length <= 1 || gameInfo.undosLeft <= 0){
    alert("cannot undo last move");
    return;
  }
  gameInfo.undosLeft -= 1;
  gameInfo.movesLeft += 1;
  gameInfo.path = gameInfo.path.slice(0, gameInfo.path.length-1);
  gameInfo.curWord = gameInfo.path[gameInfo.path.length-1];
  getWordInfo(gameInfo.curWord);
}

function handleWin(){
  //alert("GAME WON!!!!!");
  setWinComponent(gameInfo.path);
  disableGameSection();
}

function handleLose(){
  //alert("You LOSE!!!!!");
  setLoseComponent(gameInfo.tgtPath);
  disableGameSection();
}

function startGameLoad(){
  getRandomWord();
}


const root = ReactDOM.createRoot(document.getElementById('root'));
const app = <App />;
root.render(app);

/*
gameInfo = {
    "gameName": "Synonyms",
    "movesLeft": "1",
    "undosLeft": "6",
    "startWord": "pommel",
    "curWord": "pommel",
    "tgtWord": "biff",
    "tgtPath": [
        "pommel",
        "pummel",
        "biff",
        "poke",
        "thump",
        "biff"
    ],
    "path": [
        "pommel"
    ],
    "selectionList": {
        "synonyms": [
          "pummel",
          "saddlebow",
          "knob",
          "biff"
        ],
        "antonyms": [
            "grimley"
        ]
    }
}
updateGameInfoDisplays();*/


startGameLoad();