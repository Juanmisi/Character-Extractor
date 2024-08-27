<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Juanmisi/Character-Extractor">
    <img src="images/Logo.png" alt="Logo" width="280" height="100">
  </a>

<h3 align="center">Modelos de lenguaje aplicados a procesos de Big Data</h3>

  <p align="center">
    Esta guía inicial mostrará cómo instalar y ejecutar la herramienta de detección de personajes en obras literias. El proyecto necesitará tener disponibles APIs de OpenAI por parte de los usuarios.
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de Contenidos</summary>
  <ol>
    <li>
      <a href="#Sobre el proyecto">Sobre el proyecto</a>
    </li>
    <li>
      <a href="#Pasos iniciales">Pasos iniciales</a>
      <ul>
        <li><a href="#Requisitos">Requisitos</a></li>
        <li><a href="#Instalación">Instalación</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- Sobre el proyecto -->
## Sobre el proyecto

EL siguiente proyecto permite obtener descripciones de personajes de una obra literaria en inglés mediante el uso de modelos de lenguaje.
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Pasos iniciales -->
## Pasos iniciales

Para obtener una copia del proyecto y ejecutar localmente se deben seguir los siguientes pasos.


### Requisitos

El proyecto utiliza Python 3.11.4 para ejecutarse, se recomienda tanto el uso de esta versión de python como el uso de los paquetes listados en requirements instalando con pip los paquetes en un entorno virtual.
* cmd
  ```sh
  pip install -r ./requirements.txt
  ```

### Instalación

1. Debemos tener una API key de OpenAI con nuestra cuenta. Hay que tener en cuenta que se aplicarán cargos al hacer uso de los LLMs.
2. Clonamos el repositorio
   ```sh
   git clone https://github.com/Juanmisi/Character-Extractor.git
   ```
3. Activamos el entorno virtual en el que hemos instalado los paquetes.
   ```sh
   .\.venv\Scripts\activate
   ```
4. Creamos un .env donde almacenaremos las API keys.
5. Metemos la obra u obras que deseemos analizar en la carpeta books
6. Especificamos el modelo y la versión a usar en las líneas 23 y 24 de main.py
7. Al ejecutar los resultados aparecerán en la carpeta characters_list

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/Juanmisi/Character-Extractor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Juanmisi/Character-Extractor" alt="contrib.rocks image" />
</a>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Juanmisi/Character-Extractor.svg?style=for-the-badge
[contributors-url]: https://github.com/Juanmisi/Character-Extractor/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Juanmisi/Character-Extractor.svg?style=for-the-badge
[forks-url]: https://github.com/Juanmisi/Character-Extractor/network/members
[stars-shield]: https://img.shields.io/github/stars/Juanmisi/Character-Extractor.svg?style=for-the-badge
[stars-url]: https://github.com/Juanmisi/Character-Extractor/stargazers
[issues-shield]: https://img.shields.io/github/issues/Juanmisi/Character-Extractor.svg?style=for-the-badge
[issues-url]: https://github.com/Juanmisi/Character-Extractor/issues
[license-shield]: https://img.shields.io/github/license/Juanmisi/Character-Extractor.svg?style=for-the-badge
[license-url]: https://github.com/Juanmisi/Character-Extractor/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
