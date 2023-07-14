function App() {
  return (
    <div className="app">
      <TitleSection />
      <InputSection />
      <InfoSection />
      <BottomSection />
    </div>
  );
}

function TitleSection() {
  return (
    <div className="title-section">
      <h1>AI Dietician</h1>
    </div>
  );
}


function InputSection() {
  return (
    <div className="input-section full-view">
      <InputForm />
    </div>
  );
}

function InputForm() {
  return (
    <div className="input-form">
      <form action="javascript:submitInput();">
        <div className="input-form-info">
          <label for="ipf-age">Age:</label>
          <input type="number" id="ipf-age" name="ipf-age" defaultValue="20" />

          <label for="ipf-gender">Sex:</label>
          <select type="text" id="ipf-gender" name="ipf-gender">
            <option value="male">Male</option>
            <option value="female">Female</option>
          </select>

          <label for="ipf-height">Height (cm):</label>
          <input type="number" id="ipf-height" name="ipf-height" defaultValue="180" />

          <label for="ipf-weight">Weight (kg):</label>
          <input type="number" id="ipf-weight" name="ipf-weight" defaultValue="90" />

          <label for="ipf-ex-amt">Exercise Amount:</label>
          <select type="text" id="ipf-ex-amt" name="ipf-ex-amt">
            <option value="1.2">0 times/week</option>
            <option value="1.375">1-3 times/week</option>
            <option value="1.55">4-5 times/week</option>
            <option value="1.725">6+ times/week</option>
          </select>

          <label for="ipf-goal">Goal:</label>
          <select type="text" id="ipf-goal" name="ipf-goal">
            <option value="Lose Weight">Lose Weight</option>
            <option value="Maintain Weight">Maintain Weight</option>
            <option value="Gain Weight">Gain Weight</option>
          </select>
        </div>
        <div className="input-form-submit">
          <input type="submit" value="Submit" />
        </div>
      </form>
    </div>
  );
}

var userInfoUpdate;
class InfoSection extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      bmi: "99",
      bmr: "9999",
      calGoal: "9999",
      goal: "TMP goal"
    }
  }
  componentDidMount() {
    userInfoUpdate = (info) => {
      this.setState({ bmi: info.bmi });
      this.setState({ bmr: info.bmr });
      this.setState({ calGoal: info.calGoal });
      this.setState({ goal: info.goal });
    };
  }
  render() {
    return (
      <div className="info-section hidden">
        <p>BMI: {parseFloat(this.state.bmi).toFixed(2)}</p>
        <p>BMR: {parseFloat(this.state.bmr).toFixed(0)}</p>
        <p>Cals/Day: {parseFloat(this.state.calGoal).toFixed(0)}</p>
        <p>Selected Goal: {this.state.goal}</p>
      </div>
    );
  }
}

function BottomSection() {
  return (
    <div className="bottom-section hidden">
      <FoodCard idx='0' fName="Water" calCount="0" imgUrl="https://domf5oio6qrcr.cloudfront.net/medialibrary/7909/conversions/b8a1309a-ba53-48c7-bca3-9c36aab2338a-thumb.jpg" />
      <FoodCard idx='1' fName="A Lot of Bread" calCount="1500" imgUrl="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Korb_mit_Br%C3%B6tchen.JPG/1200px-Korb_mit_Br%C3%B6tchen.JPG" />
      <FoodCard idx='2' fName="Some Hardtack" calCount="250" imgUrl="https://breaddad.com/wp-content/uploads/2020/05/bread-hardtack-6-e1588416642875-500x375.jpg" />
      <FitnessCard idx='0' fName="Fitness Required" />
    </div>
  );
}

var foodUpdateFuncs = {};
class FoodCard extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      idx: props.idx,
      fName: props.fName,
      calCount: props.calCount,
      imgUrl: props.imgUrl,
      fat: "0g",
      sugar: "0g",
      carb: "0g",
      protien: "0g",
      desc: 'TODO'
    }
  }
  componentDidMount() {
    foodUpdateFuncs[this.state.idx] = (food) => {
      this.setState({
        fName: food.name,
        calCount: food.cal,
        imgUrl: food.img,
        fat: food.fat,
        sugar: food.sugar,
        carb: food.carb,
        protien: food.protien,
        desc: food.desc
      });
    };
  }
  render() {
    return (
      <div className="food-card">
        <div className="food-card-front food-card-face">
          <FoodInfo fName={this.state.fName} calCount={this.state.calCount} />
          <FoodImg imgUrl={this.state.imgUrl} fName={this.state.fName} />
        </div>
        <div className="food-card-back food-card-face">
          <FoodInfo fName={this.state.fName} calCount={this.state.calCount} />
          <FoodInfoExtended fName={this.state.fName} fat={this.state.fat} sugar={this.state.sugar} carb={this.state.carb} protien={this.state.protien} desc={this.state.desc} />
        </div>
      </div>
    );
  }
}


function FoodInfo(props) {
  return (
    <div className="food-info">
      <h1>{props.fName}</h1>
      <h3>{props.calCount} Calories</h3>
    </div>
  );
}

function FoodImg(props) {
  return (
    <div className="food-img-section">
      <img className="food-img" src={props.imgUrl} alt={props.fName + " Image"} />
    </div>
  );
}

function FoodInfoExtended(props) {
  return (
    <div className="food-info-extended">
      <h2>Macronutrients</h2>
      <p>Fat: {props.fat}</p>
      <p>Sugar: {props.sugar}</p>
      <p>Carbs: {props.carb}</p>
      <p>Protien: {props.protien}</p>
      <br />
      <br />
      <p>{props.desc}</p>
    </div>
  );
}

var userexcersieUpdate = {};
class FitnessCard extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      idx: props.idx,
      activityName: props.activityName,
      duration: props.duration,
      imgSrc: props.imgSrc,
      activityName2: props.activityName2,
      duration2: props.duration2,
      imgSrc2: props.imgSrc2

    }
  }
  componentDidMount() {
    userexcersieUpdate[this.state.idx] = (fitnessrecords, fitnessrecords2) => {
      this.setState({
        activityName: fitnessrecords.name,
        duration: fitnessrecords.duration,
        imgSrc: fitnessrecords.img,
        activityName2: fitnessrecords2.name,
        duration2: fitnessrecords2.duration,
        imgSrc2: fitnessrecords2.img
      })
    };
  }

  render() {
    return (
      <div className="fitness-card">
        <div className="fitness-card-front fitness-card-face">
          <FitnessInfo activityName={this.state.activityName} duration={this.state.duration} />
          <FitnessImg imgSrc={this.state.imgSrc} activityName={this.state.activityName} />
        </div>
        <div className="fitness-card-back fitness-card-face">
          <FitnessInfo activityName={this.state.activityName2} duration={this.state.duration2} />
          <FitnessImg imgSrc={this.state.imgSrc2} activityName={this.state.activityName2} />
        </div>
      </div>
    );
  }
}

function FitnessInfo(props) {
  return (
    <div className="fitness-info">
      <h2>Recommended Activity: {props.activityName}</h2>
      <p>Duration: {props.duration}</p>
    </div>
  );
}

function FitnessImg(props) {
  return (
    <div className="fitness-img-section">
      <img className="fitness-img" src={props.imgSrc} alt={props.activityName} />
    </div>
  );
}


var fullViewActive = true
function submitInput() {
  if (fullViewActive) {
    toggleView();
    fullViewActive = false;
  }
  //commented to save api calls
  requestDietInfo();
}

//for view changing
function toggleView() {
  var inputs = document.querySelectorAll('.input-section');
  [...inputs].forEach((input) => {
    input.classList.toggle('full-view');
  });

  var bottomSections = document.querySelectorAll('.bottom-section');
  [...bottomSections].forEach((bs) => {
    bs.classList.toggle('hidden');
  });

  var infoSections = document.querySelectorAll('.info-section');
  [...infoSections].forEach((is) => {
    is.classList.toggle('hidden');
  });
}

var dietInfo = {
  'bmi': 99,
  'bmr': 99,
  'calGoal': 99,
  'goal': '99'
};

var excersieinfo = {
  'duration': 99,
  'excersie': 99
};

function updateDietInfoDisplays() {
  userInfoUpdate(dietInfo);

  foodUpdateFuncs[0](dietInfo.foods.bfood);
  foodUpdateFuncs[1](dietInfo.foods.lfood);
  foodUpdateFuncs[2](dietInfo.foods.dfood);
  userexcersieUpdate[0](dietInfo.fitnessrecord_1, dietInfo.fitnessrecord_2);
}


//URL for API requests
var actionUrl =
  'backend/backendCode.py'

function requestDietInfo() {
  var vdata = {};
  vdata.age = document.getElementById("ipf-age").value;
  vdata.gender = document.getElementById("ipf-gender").value;
  vdata.height = document.getElementById("ipf-height").value / 100;
  vdata.weight = document.getElementById("ipf-weight").value;
  vdata.activityLev = document.getElementById("ipf-ex-amt").value;
  vdata.goal = document.getElementById("ipf-goal").value;
  $.ajax({
    type: "GET",
    url: actionUrl,
    data: vdata,
    crossDomain: true,
    dataType: 'json',
    success: function (data) {
      dietInfo.bmi = data.bmi;
      dietInfo.bmr = data.bmr;
      dietInfo.calGoal = data.calGoal;
      dietInfo.goal = data.goal;
      dietInfo.foods = data.foods;
      dietInfo.fitnessrecord_1 = data.fitnessrecord_1;
      dietInfo.fitnessrecord_2 = data.fitnessrecord_2;
      updateDietInfoDisplays();
    }
  });
}


ReactDOM.render(<App />, document.getElementById('root'));


//for card flipping
var cards = document.querySelectorAll('.food-card');

[...cards].forEach((card) => {
  card.addEventListener('click', function () {
    card.classList.toggle('is-flipped');
  });
});

var cards = document.querySelectorAll('.fitness-card');

[...cards].forEach((card) => {
  card.addEventListener('click', function () {
    card.classList.toggle('is-flipped');
  });
});

