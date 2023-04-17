import java.security.*;
import java.security.spec.*;
import javax.crypto.*;
import java.util.Base64;

public class DigitalSignature {
    private static final String ALGORITHM = "SHA256withRSA";

    public static void main(String[] args) throws Exception {
        // Generate a key pair
        KeyPairGenerator keyGen = KeyPairGenerator.getInstance("RSA");
        keyGen.initialize(2048);
        KeyPair keyPair = keyGen.generateKeyPair();

        // Create a signature object
        Signature signature = Signature.getInstance(ALGORITHM);
        signature.initSign(keyPair.getPrivate());

        // Create a message to sign
        String message = "Hello, world!";
        byte[] messageBytes = message.getBytes("UTF-8");

        // Sign the message
        signature.update(messageBytes);
        byte[] signatureBytes = signature.sign();

        // Print the signature
        String signatureBase64 = Base64.getEncoder().encodeToString(signatureBytes);
        System.out.println("Signature: " + signatureBase64);

        // Verify the signature
        signature.initVerify(keyPair.getPublic());
        signature.update(messageBytes);
        boolean verified = signature.verify(signatureBytes);

        System.out.println("Verified: " + verified);
    }
}
