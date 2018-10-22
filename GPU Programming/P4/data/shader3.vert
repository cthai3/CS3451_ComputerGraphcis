#define PROCESSING_TEXTURE_SHADER

uniform mat4 transform;
uniform mat4 texMatrix;

attribute vec4 position;
attribute vec4 color;
attribute vec3 normal;
attribute vec2 texCoord;

varying vec4 vertColor;
varying vec4 vertTexCoord;

uniform sampler2D texture;

void main() {
	vertColor = color;
  	vec4 pos = position;
	vertTexCoord = texMatrix * vec4(texCoord, 1.0, 1.0);

   	vec4 textColor = texture2D(texture, vertTexCoord.st) * vertColor;

    	float intensity = (textColor.r) * 0.3 + (textColor.g) * 0.6 + (textColor.b) * 0.1;

    	pos += vec4(normal * intensity * 200, 0.0);

    	gl_Position = transform * pos;
}
