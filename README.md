<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Strong-Lab/VirKraken">
    <img src="images/logo.jpg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">VirKraken</h3>

  <p align="center">
    An extension to identify viral elements in Kraken 2 outputs
    <br />
    <a href="https://github.com/Strong-Lab/VirKraken/issues">Report Bug</a>
    ·
    <a href="https://github.com/Strong-Lab/VirKraken/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-virkraken">About VirKraken</a>
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
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About VirKraken

This project was created to identify viral contigs using [Kraken 2](https://example.com) in the publication [Cite](https://example.com). This extension allows a user to get the headers of viral elements and provides the ability to retain only those headers or remove them if the sequencing file is provided. 


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

VirKraken requires Python 3 and the following libraries (if installling through pip, libraries are automatically install)
* pandas
* scikit-learn
* biopython
* importlib-resources


### Installation

VirKraken is aviliable on [PyPI](https://pypi.org/project/virkraken/) and can be forked on this repository. The easiest way to install VirKraken is to use pip. 

```
pip install virkraken
```

<!-- USAGE EXAMPLES -->
## Usage
VirKraken works as a command line script. Once install via pip, virkraken the command can be accessed. To get the help screen type:
```
virkraken -h
```

The paramters of VirKraken are:
* -f: Kraken output file \[required]
* -c: Seqeuncing file to parse \[optional]
* -r: Remove viral elements flag
* -o: Rename output files \[optional]


**Running VirKraken** 

VirKraken without a sequencing file and renaming the output
```
virkraken -f Kraken_Output.txt -o Viral_Sequences
```
The script above will return Viral_Sequences.csv which will contain a column of sequnce headers and NCBI TaxIDs. All returned sequence headers are viral. 

VirKraken to filter a seqeunce file
```
virkraken -f Kraken_Output.txt -c final.contigs.fa -o Viral_Sequences
```
The script above will return Viral_Sequences.csv and Viral_Sequences.fasta. All returned sequences are viral. VirKraken will filter the input fasta for sequence headers matching the predicted viral headers. 

VirKraken to remove viral sequences
```
virkraken -r -f Kraken_Output.txt -c final.contigs.fa -o Filtered_Sequences
```
Seqeunce headers that are assigned a viral designation are removed from the resulting fasta file output. 

<!-- ROADMAP -->
## Roadmap

<p align="center">
    Current Version: 0.0.5
</p>

Improvements to be made:
- Fix .gz contig fasta outfile
- Allow paired .fastq input
- Integrate into Kraken 2 codebase


See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Cody Glickman - [@glickman_Cody](https://twitter.com/glickman_cody) - glickman.cody@gmail.com

Project Link: [https://github.com/Strong-Lab/VirKraken](https://github.com/Strong-Lab/VirKraken)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Img Shields](https://shields.io)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Strong-Lab/VirKraken.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Strong-Lab/VirKraken.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/Strong-Lab/VirKraken.svg?style=for-the-badge
[stars-url]: https://github.com/Strong-Lab/VirKraken/stargazers
[issues-shield]: https://img.shields.io/github/issues/Strong-Lab/VirKraken.svg?style=for-the-badge
[issues-url]: https://github.com/Strong-Lab/VirKraken/issues
[license-shield]: https://img.shields.io/github/license/Strong-Lab/VirKraken.svg?style=for-the-badge
[license-url]: https://github.com/Strong-Lab/VirKraken/LICENSE.txt
[product-screenshot]: images/screenshot.png

