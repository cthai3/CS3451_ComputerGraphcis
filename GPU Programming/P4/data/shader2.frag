#define PROCESSING_COLOR_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
	gl_FragColor = vec4(1.0, vertTexCoord.t, vertTexCoord.t, 1.0);

	float a = ((float(vertTexCoord.x) * 3.0) - 2.1);
	float b = ((float(vertTexCoord.y) * 3.0) - 1.5);

	float realArea = 0.0;
	float imaginArea = 0.0;

	for (int i = 0; i < 20; i++) {
    		float temporaryR = (float(realArea * realArea)) - (float(imaginArea * imaginArea));
    		float temporaryI = 2.0 * realArea * imaginArea;

    		realArea = temporaryR + a;
    		imaginArea = temporaryI + b;

    		float distance = sqrt((realArea * realArea) + (imaginArea * imaginArea));
    			if (distance > 2) {
        			gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
        			return;
    			}
	}

	gl_FragColor = vec4(1.0, 1.0, 1.0, 1.0);
}