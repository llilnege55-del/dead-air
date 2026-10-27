"""Convert the web version of Dead Air (Google Fonts) into the app version (bundled fonts)."""
import re,sys
src=open(sys.argv[1]).read();out=sys.argv[2]
fonts='''<style>
@font-face{font-family:'VT323';src:url(fonts/VT323-Regular.ttf) format('truetype');font-weight:400}
@font-face{font-family:'Rock Salt';src:url(fonts/RockSalt-Regular.ttf) format('truetype');font-weight:400}
@font-face{font-family:'Rajdhani';src:url(fonts/Rajdhani-Medium.ttf) format('truetype');font-weight:500}
@font-face{font-family:'Rajdhani';src:url(fonts/Rajdhani-SemiBold.ttf) format('truetype');font-weight:600}
@font-face{font-family:'Rajdhani';src:url(fonts/Rajdhani-Bold.ttf) format('truetype');font-weight:700}
@font-face{font-family:'IBM Plex Mono';src:url(fonts/IBMPlexMono-Regular.ttf) format('truetype');font-weight:400}
@font-face{font-family:'IBM Plex Mono';src:url(fonts/IBMPlexMono-SemiBold.ttf) format('truetype');font-weight:600}
</style>'''
src=re.sub(r'<link rel="preconnect"[^>]*>\n','',src)
src=re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com[^>]*>',fonts,src)
src=src.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
assert 'googleapis' not in src
a="<dt>ESC</dt><dd>Pause</dd>"
if a in src and 'F11' not in src: src=src.replace(a,a+"\n        <dt>F11</dt><dd>Toggle fullscreen</dd>")
head='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob:; font-src 'self'; media-src 'self' data: blob:">
<style>:root{color-scheme:dark}body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}</style>
'''
i=src.index('</style>')+8
open(out,'w').write(head+src[:i]+'\n</head>\n<body>\n'+src[i:]+'\n</body>\n</html>\n')
