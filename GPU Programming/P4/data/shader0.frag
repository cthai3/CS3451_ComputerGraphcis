#define PROCESSING_COLOR_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {

	for (int a = 0; a < 3; a++) {

          for (int b = 0; b < 3; b++) {
            float x = (float(1.0 / 3.0) * a) + float(1.0 / 6.0) ;
            float y = (float(1.0 / 3.0) * b) + float(1.0 / 6.0);
            float distance = sqrt(((x - float(vertTexCoord.x)) * (x - float(vertTexCoord.x))) + ((y - float(vertTexCoord.y)) * (y - float(vertTexCoord.y))));

            if (distance < 0.1111) {
                gl_FragColor = vec4(0.2, 0.4, 1.0, 0.0);
                return;
            } else {
                gl_FragColor = vec4(0.2, 0.4, 1.0, 0.8);
            }
        }
    }
}

