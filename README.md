<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Instagra][instagram-shield]][instagram-url]



<br />
<div align="center">
  <h1 align="center">typefast</h1>

  <p align="center">
    A CLI application for measuring your typing speed.l
    <br />
    <a href="https://github.com/Neihtq/typefast/issues">Report Bug or Request Feature</a>
  </p>
</div>


<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![](demo/demo.mp4)

Measuring typing speed is a fun and diverting activity that can be done in a short amount of time. When taking a break, too short for playing games or watching series, but too long to only drink a cup of water, speed typing is ideal. However, mostly typing speed can be measured on websites such as [https://10fastfingers.com/typing-test/](10fastfingers) or [https://monkeytype.com](monkeytype). While they do the job, they require a browser, javascript, or even cookies. 

Typefast is a CLI application that does the same like monketype, but in the terminal! It is cross platform and binds in well in the terminal. Starting and doing a few quick speed typing test has never been smoother. It collects random quotes from [https://www.brainyquote.com/](BrainyQuote) for typing tests. Other speed tests like most words within a minute, etc. are WIP. It is very lightweight and uses very little dependencies.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [https://www.python.org/](Python3)
* [https://pypi.org/project/beautifulsoup4/](Beautiful Soup)
* [https://pypi.org/project/tqdm/](tqdm)
* [https://pypi.org/project/requests/](Requests)
* [https://docs.python.org/3/howto/curses.html](curses)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* Have pip installed (different methodes explained [https://pip.pypa.io/en/stable/installation/](here))
    ```sh
    python -m ensurepip --upgrade
    ```
* upgrade pip to its most recent version
    ```sh
    pip install --upgrade pip
    ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Neihtq/typefast
   cd typefast
   ```
2. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
3. Run application
   ```sh
   python main.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
* The timer will only start after the first character has been entered
* Hitting the space button will submit the current word and therefore you cannot edit the previous input anymore (e.g. deleting with backspace)
* This application calculates your Words per minute (WPM) metric. Other metrics are WIP
* After finishing a test, it will automatically start a new one after 5 seconds
* You can restart with a new quote by pressing `esc` key

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Add Changelog
- [ ] Different modes
    - [ ] Enter many words within a minute
- [ ] Make typefast von usr/bin executable i.e. typefast as a command
- [ ] Add tests
- [ ] Add different metrics
- [ ] Multi-language Support

See the [open issues](https://github.com/Neihtq/typefast/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue.
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Quang Thien Nguyen - q.thien.nguyen@outlook.de - [LinkedIn](https://www.linkedin.com/in/thien-quang-nguyen/) - [@neiht (Instagram)](https://www.instagram.com/neiht/)

Project Link: [https://github.com/Neihtq/typefast](https://github.com/Neihtq/typefast)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/neihtq/typefast.svg?style=for-the-badge
[contributors-url]: https://github.com/neihtq/typefast/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/neihtq/typefast.svg?style=for-the-badge
[forks-url]: https://github.com/neihtq/typefast/network/members
[stars-shield]: https://img.shields.io/github/stars/neihtq/typefast.svg?style=for-the-badge
[stars-url]: https://github.com/neihtq/typefast/stargazers
[issues-shield]: https://img.shields.io/github/issues/neihtq/typefast.svg?style=for-the-badge
[issues-url]: https://github.com/neihtq/typefast/issues
[license-shield]: https://img.shields.io/github/license/neihtq/typefast.svg?style=for-the-badge
[license-url]: https://github.com/neihtq/typefast/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/thien-quang-nguyen/
[instagram-shield]: https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white
[instagram-url]: https://www.instagram.com/neiht/
[product-screenshot]: demo/demo.mp4