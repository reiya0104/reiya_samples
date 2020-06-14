// This is a JavaScript file named "config.js"
window.MathJax = {
    TeX: {
        equationNumbers: {autoNumber: "AMS"},
        inlineMath: [
            ["$", "$"],
            ["\\(", "\\)"]
        ],
        displayMath: [             // start/end delimiter pairs for display math
            ['$$', '$$'],
            ['\\[', '\\]']
        ],
        processEscapes: true,
        Macros: {
            x: "{\\times}",
            bm: ["{\\boldsymbol{#1}}",1],
            dd: ["{\\frac{\\partial #1}{\\partial #2}}",2],
            mat: ["{\\begin{pmatrix} #1 & #2 \\\\ #3 & #4 \\end{pmatrix}}",4]
        }
    },
    CommonHTML: {
        scale: 90,
        mtextFontInherit: true
    }
};