/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',  // Enables dark: variants
  content: [
    "./templates/**/*.html",
    "./*/templates/**/*.html", 
    "./**/*.py"
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eef2ff',
          500: '#6366f1',  // Indigo accent
          900: '#1e1b4b',
        }
      }
    },
  },
  plugins: [],
}

