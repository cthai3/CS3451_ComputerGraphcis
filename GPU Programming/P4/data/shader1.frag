#define PROCESSING_TEXTURE_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

uniform sampler2D texture;

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
	//given
	vec4 diffuse_color = texture2D(texture, vertTexCoord.xy);

	float greyCent = (diffuse_color.r) * 0.3 + (diffuse_color.g) * 0.6 + (diffuse_color.b) * 0.1;

	vec2 upPos = vec2(vertTexCoord.x, vertTexCoord.y + .01);
	vec2 downPos = vec2(vertTexCoord.x, vertTexCoord.y - .01);

	vec2 rightPos = vec2(vertTexCoord.x + .01, vertTexCoord.y);
	vec2 leftPos = vec2(vertTexCoord.x - .01, vertTexCoord.y);
	
	
	vec4 up = texture2D(texture, upPos.xy);
	vec4 down = texture2D(texture, downPos.xy);

	vec4 right = texture2D(texture, rightPos.xy);
	vec4 left = texture2D(texture, leftPos.xy);
	
	float greyU = (up.r) * 0.3 + (up.g) * 0.6 + (up.b) * 0.1;
	float greyD = (down.r) * 0.3 + (down.g) * 0.6 + (down.b) * 0.1;
	
	float greyR = (right.r) * 0.3 + (right.g) * 0.6 + (right.b) * 0.1;
	float greyL = (left.r) * 0.3 + (left.g) * 0.6 + (left.b) * 0.1;


	float edgeDetection = (greyU + greyD + greyR + greyL) - (4 * greyCent);

	vec4 edgeColor = vec4(edgeDetection, edgeDetection, edgeDetection, 1);
	//given
	gl_FragColor = vec4(edgeDetection * 3, edgeDetection * 3, edgeDetection * 3, 1.0);
}

