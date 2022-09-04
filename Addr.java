import lombok.Data;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;
//자바 어노테이션 ->자바한테 말해주는 메세지

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Addr {
	private int idx;
	private String name;
	private String address;
	private String phone;
	private String regDate;

