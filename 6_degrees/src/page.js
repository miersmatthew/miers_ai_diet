
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

function GameCards() {
  return (
    <div className="game-cards">
      <GameCard title="Synonyms" description="Find a path to the target word using synonyms only." gamemode="1"/>
      <GameCard title="Synonyms and Antonyms" description="Find a path to the target word using both synonyms and antonyms only." gamemode="2"/>
    </div>
  );
}

class GameCard extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      title: props.title,
      description: props.description,
      gamemode: props.gamemode,
      numMoves: 6,
      flipped: false
    }
  }

  routeChange=()=> {
    window.location.href=`gamepage.html?gm=${this.state.gamemode}&moves=${this.state.numMoves}`;
  }

  toggleFlipped=()=> {
    this.setState({ flipped: !this.state.flipped});
  }

  handleClick = e => {
    e.stopPropagation();
  }

  render() {
    return (
      <div className={`game-card ${this.state.flipped ? 'is-flipped': null}`} onClick={this.toggleFlipped}>
        <div className="card-front card-face">
          <div className="card-content">
            <div className="card-content-title">
              <p>{ this.state.title }</p>
            </div>
          </div>
        </div>
        <div className="card-back card-face">
          <div className="card-content">
            <div className="card-content-description">
              <p>{ this.state.description }</p>
            </div>
            <div className="card-content-settings" onClick={this.handleClick}>
              <p>Number of moves:</p>
              <input type='number' defaultValue='6' onChange={ e => this.setState({numMoves: e.target.value}) } ></input>
            </div>
            <div className="card-content-button" onClick={this.handleClick}>
              <button onClick={this.routeChange} >Start</button>
            </div>
          </div>
        </div>
      </div>
    );
  }
}



class App extends React.Component {
  constructor(props) {
    super();
  }
  render() {
    return (
      <div className="app">
        <TitleSection />
        <GameCards />
      </div>
    );
  }
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

const root = ReactDOM.createRoot(document.getElementById('root'));
const app = <App />;
root.render(app);


$('button selector').click(function(){
  window.location.href='the_link_to_go_to.html';
})