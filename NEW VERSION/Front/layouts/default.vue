<template>
  <div>
    <Nuxt />
  </div>
</template>

<style>

::-webkit-scrollbar {
    width: 10px;
}
::-webkit-scrollbar-track {
    background: #e1fdff;
}
::-webkit-scrollbar-thumb {
    background: rgb(0, 89, 255);
}
::-webkit-scrollbar-thumb:hover {
    background: rgb(3, 137, 247);
}
 
 
html {
  font-family:
    'Source Sans Pro',
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    'Helvetica Neue',
    Arial,
    sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
}
@font-face {
    font-family: 'Exo2-Thin';
    src: url('/assets/fonts/Exo2-Thin.ttf') format("truetype");
}
@font-face {
    font-family: 'Exo2-Light';
    src: url('/assets/fonts/Exo2-Light.ttf') format("truetype");
}
@font-face {
    font-family: 'Exo2-Medium';
    src: url('/assets/fonts/Exo2-Medium.ttf') format("truetype");
}
@font-face {
    font-family: 'Exo2-Bold';
    src: url('/assets/fonts/Exo2-Bold.ttf') format("truetype");
}

</style>
