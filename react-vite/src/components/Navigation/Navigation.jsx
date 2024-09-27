import { useState } from "react";
import { NavLink, useNavigate } from "react-router-dom";
import { FaSearch } from "react-icons/fa";
import { useDispatch } from "react-redux";
import ProfileButton from "./ProfileButton";
import { getSearchLabel } from "../../redux/searchLabel";
import "./Navigation.css";

function Navigation() {
	const [searchLabel, setSearchLabel] = useState("");
	const navigate = useNavigate()
	const dispatch = useDispatch()

	return (
		<ul className="nav">
			<div className="left">
				<NavLink className="navs" to="/">
					<li>Home</li>
				</NavLink>
				<NavLink className="navs" to="/explore" onClick={() => dispatch(getSearchLabel(""))}>
					<li>Explore</li>
				</NavLink>
				{/* TODO: MAKE DROPDOWN THAT SAYS STASH OR IMG, ONLY VISIBLE TO A LOGGED IN USER */}
				<NavLink className="navs" to="/stashes/new">
					<li>Create</li>
				</NavLink>
			</div>
			<div className="search-cont">
				<input 
					className="search" 
					type="search" 
					placeholder="Search for images by label" 
					value={searchLabel}
					onChange={(e) => setSearchLabel(e.target.value)}
				/>
				<button 
					onClick={() => {
						dispatch(getSearchLabel(searchLabel))
						navigate(`/explore`)
					}}
				>
					<FaSearch />
				</button>
			</div>
			<div>
				<li className="right">
					<ProfileButton />
				</li>
			</div>
		</ul>
	);
}

export default Navigation;
